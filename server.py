import pandas as pd
import seaborn as sns
import plotly.express as px
from dash import Dash, dcc, html, dash_table, callback, Output, Input
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP, "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

df = sns.load_dataset('penguins')

# Adding a custom background image
app.layout = html.Div(
    style={'background-color': '#F3E9D2', 'font-family': 'Poppins, sans-serif', 'height': '100vh'},
    children=[
        dbc.Container(
            [
                html.H4(children='DataFrame',style={'text-align': 'left', 'color': '#283044', 'margin-top': '20px', 'font-size': '24px', 'font-family': 'Poppins, sans-serif', 'font-weight': 'bold'}),
                dash_table.DataTable(
                    data=df.to_dict('records'),
                    page_size=10,
                    style_cell={'textAlign': 'left', 'min-width': '150px', 'width': '150px', 'max-width': '150px', 'font-family': 'Arial, sans-serif', 'font-size': '16px', 'color': '#283044'},
                    style_header={'backgroundColor': '#F7D6BF', 'color': '#283044', 'font-family': 'Arial, sans-serif', 'font-size': '18px'},
                    style_as_list_view=True,
                ),
                html.Hr(),
                html.H4(children='Boxplot', style={'text-align': 'center', 'color': '#283044', 'margin-top': '20px', 'font-size': '24px', 'font-family': 'Poppins, sans-serif', 'font-weight': 'bold'}),
                dbc.Row(
                    [
                        dbc.Col(dcc.Dropdown(options=[{'label': col, 'value': col} for col in df.columns], value=df.columns[0], id='x-axis-column-box', style={'font-size': '16px', 'width': '100%'}), width=4),
                        dbc.Col(dcc.Dropdown(options=[{'label': col, 'value': col} for col in df.columns], value=df.columns[1], id='y-axis-column-box', style={'font-size': '16px', 'width': '100%'}), width=4),
                        dbc.Col(dcc.Dropdown(options=[{'label': col, 'value': col} for col in df.columns], value=df.columns[-1], id='color-column-box', style={'font-size': '16px', 'width': '100%'}), width=4),
                    ]
                ),
                html.Div(id='graph-box-container'),
                html.Hr(),
                html.H4(children='Scatterplot', style={'text-align': 'center', 'color': '#283044', 'margin-top': '20px', 'font-size': '24px', 'font-family': 'Poppins, sans-serif', 'font-weight': 'bold'}),
                dbc.Row(
                    [
                        dbc.Col(dcc.Dropdown(options=[{'label': col, 'value': col} for col in df.columns], value=df.columns[0], id='x-axis-column-scatter', style={'font-size': '16px', 'width': '100%'}), width=4),
                        dbc.Col(dcc.Dropdown(options=[{'label': col, 'value': col} for col in df.columns], value=df.columns[1], id='y-axis-column-scatter', style={'font-size': '16px', 'width': '100%'}), width=4),
                        dbc.Col(dcc.Dropdown(options=[{'label': col, 'value': col} for col in df.columns], value=df.columns[-1], id='color-column-scatter', style={'font-size': '16px', 'width': '100%'}), width=4),
                    ]
                ),
                html.Div(id='graph-scatter-container'),
                html.Hr(),
                html.H4(children='Histogram', style={'text-align': 'center', 'color': '#283044', 'margin-top': '20px', 'font-size': '24px', 'font-family': 'Poppins, sans-serif', 'font-weight': 'bold'}),
                dbc.Row(
                    [
                        dbc.Col(dcc.Dropdown(options=[{'label': col, 'value': col} for col in df.columns], value=df.columns[1], id='x-axis-column-hist', style={'font-size': '16px', 'width': '100%'}), width=6),
                        dbc.Col(dcc.Dropdown(options=[{'label': col, 'value': col} for col in df.columns], value=df.columns[-1], id='color-column-hist', style={'font-size': '16px', 'width': '100%'}), width=6),
                    ]
                ),
                html.Div(id='graph-hist-container'),
            ],
            fluid=True,
            style={'background-color': '#F3E9D2', 'padding': '20px', 'border-radius': '10px'}
        ),
    ]
)


@app.callback(
    Output('graph-scatter-container', 'children'),
    Input('x-axis-column-scatter', 'value'),
    Input('y-axis-column-scatter', 'value'),
    Input('color-column-scatter', 'value'),
)
def scatter_plot(x_axis_column, y_axis_column, color=None):
    fig = px.scatter(df, x=x_axis_column, y=y_axis_column, color=color)
    fig.update_layout(plot_bgcolor='#F3E9D2')
    return dcc.Graph(figure=fig)

@app.callback(
    Output('graph-box-container', 'children'),
    Input('x-axis-column-box', 'value'),
    Input('y-axis-column-box', 'value'),
    Input('color-column-box', 'value'),
)
def boxplot_plot(x_axis_column, y_axis_column=None, color=None):
    fig = px.box(df, x=x_axis_column, y=y_axis_column, color=color)
    fig.update_layout(plot_bgcolor='#F3E9D2')
    return dcc.Graph(figure=fig)

@app.callback(
    Output('graph-hist-container', 'children'),
    Input('x-axis-column-hist', 'value'),
    Input('color-column-hist', 'value'),
)
def histplot_plot(x_axis_column, color=None):
    fig = px.histogram(df, x=x_axis_column, color=color)
    fig.update_layout(plot_bgcolor='#F3E9D2')
    return dcc.Graph(figure=fig)

if __name__ == '__main__':
    app.run_server(debug=True)
