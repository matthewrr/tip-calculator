from django_plotly_dash import DjangoDash

from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

import dash

app = DjangoDash('SimpleExample')   # replaces dash.Dash
# app = Dash()

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
df = {1: 25, 2:50, 3:100}
# px.line(x=["a","b","c"], y=[1,3,2], title="sample figure")
px.line(x=["a","b","c"], y=[1,3,2], title="sample figure")
fig = px.line(
    x=["a","b","c"], y=[1,3,2], # replace with your own data source
    title="sample figure", height=325
)

# fig = px.box(
#     df, # replace with your own data source
#     title="sample figure", height=325
# )

# df = px.data.gapminder().query("country=='Canada'")
# fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')

# fig = px.box(plot_df, **my_dictionary)

# app.layout = html.Div([
#         html.H1(children='Title of Dash App', style={'textAlign':'center'}),
#         # dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
#         # dcc.Graph(
#         #     id='graph-content',
#         #     # style='height: 400',
#         # )
#         dcc.Graph(id="graph-content", figure=fig),
        
#         fig.update_layout(title_pad=dict(...))
#     ])
    # style={'padding': 10, 'height': '1000px', 'flex': 1})

app.layout = html.Div([
    html.H4('Displaying figure structure as JSON'),
    dcc.Graph(id="graph", figure=fig),
    dcc.Clipboard(target_id="structure"),
    html.Pre(
        id='structure',
        style={
            'border': 'thin lightgrey solid', 
            'overflowY': 'scroll',
            'height': '275px'
        }
    ),
])

# app.update_layout(height=100)

# layout = dict(
#     margin=dict(l=40, r=25, b=40, t=40),
#     hovermode="closest",
#     legend=dict(font=dict(color='#7f7f7f'), orientation="h"),
#     title=gateway_obj.location,
#     font=dict(
#         color="#7f7f7f"
#     ),
# )


# @callback(
#     Output('graph-content', 'figure'),
#     Input('dropdown-selection', 'value')
# )

@app.callback(
    dash.dependencies.Output('graph-content', 'figure'),
    [dash.dependencies.Input('dropdown-selection', 'value')])

def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')


# app.run_server(debug=True)

# app.layout = html.Div([
#     dcc.RadioItems(
#         id='dropdown-color',
#         options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
#         value='red'
#     ),
#     html.Div(id='output-color'),
#     dcc.RadioItems(
#         id='dropdown-size',
#         options=[{'label': i,
#                 'value': j} for i, j in [('L','large'), ('M','medium'), ('S','small')]],
#         value='medium'
#     ),
#     html.Div(id='output-size')

# ])

# @app.callback(
#     dash.dependencies.Output('output-color', 'children'),
#     [dash.dependencies.Input('dropdown-color', 'value')])
# def callback_color(dropdown_value):
#     return "The selected color is %s." % dropdown_value

# @app.callback(
#     dash.dependencies.Output('output-size', 'children'),
#     [dash.dependencies.Input('dropdown-color', 'value'),
#     dash.dependencies.Input('dropdown-size', 'value')])
# def callback_size(dropdown_color, dropdown_size):
#     return "The chosen T-shirt is a %s %s one." %(dropdown_size,
#                                                 dropdown_color)

# if __name__ == '__main__':
#     app.run(debug=True)