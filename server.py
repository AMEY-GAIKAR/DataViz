import pandas as pd
import seaborn as sns
import plotly.express as px
from dash import Dash, dcc, html, dash_table, callback, Output, Input
import dash_mantine_components as dmc

app = Dash(__name__)

# df = pd.read_csv('')
df = sns.load_dataset('penguins')

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app.layout = html.Div([
    html.H4(style={},children='DataFrame'),
    dash_table.DataTable(data=df.to_dict('records'),page_size=10),
    html.H4(style={},children='Boxplot'),
    html.Div([
        dcc.Dropdown(df.columns, df.columns[0], id='x-axis-column-box')
    ], style={

    }),
    html.Div([
        dcc.Dropdown(df.columns, df.columns[1], id='y-axis-column-box')
    ], style={
            
    }),
    html.Div([
        dcc.Dropdown(df.columns, df.columns[-1], id='color-column-box')
    ], style={

    }),
    dcc.Graph(id='graph-box'),
    html.H4(style={},children='Scatterplot'),
    html.Div([
        dcc.Dropdown(df.columns, df.columns[0], id='x-axis-column-scatter')
    ], style={

    }),
    html.Div([
        dcc.Dropdown(df.columns, df.columns[1], id='y-axis-column-scatter')
    ], style={

   }),
    html.Div([
        dcc.Dropdown(df.columns, df.columns[-1], id='color-column-scatter')
    ], style={

    }),
    dcc.Graph(id='graph-scatter'),
    html.H4(style={},children='Histogram'),
    html.Div([
        dcc.Dropdown(df.columns, df.columns[1], id='x-axis-column-hist')
    ], style={

   }),
    html.Div([
        dcc.Dropdown(df.columns, df.columns[-1], id='color-column-hist')
    ], style={

    }),
    dcc.Graph(id='graph-hist'),
])

@callback(
    Output('graph-scatter', 'figure'),
    Input('x-axis-column-scatter', 'value'),
    Input('y-axis-column-scatter', 'value'),
    Input('color-column-scatter', 'value')
) 
def scatter_plot(x_axis_column, y_axis_column, color=None):
    fig = px.scatter(df,x=x_axis_column,y=y_axis_column, color=color)
    return fig

@callback(
    Output('graph-box', 'figure'),
    Input('x-axis-column-box', 'value'),
    Input('y-axis-column-box', 'value'),
    Input('color-column-box', 'value')
) 
def boxplot_plot(x_axis_column, y_axis_column=None, color=None):
    fig = px.box(df,x=x_axis_column,y=y_axis_column, color=color)
    return fig

@callback(
    Output('graph-hist', 'figure'),
    Input('x-axis-column-hist', 'value'),
    Input('color-column-hist', 'value')
) 
def histplot_plot(x_axis_column, color=None):
    fig = px.histogram(df,x=x_axis_column, color=color)
    return fig

if __name__ == "__main__":
    app.run(debug=True)
