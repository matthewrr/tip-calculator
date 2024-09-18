from django.shortcuts import render
# import plotly.express as px 
import dash
# import pandas as pd
# from dash import dcc, html
from django_plotly_dash import DjangoDash
from .models import *


from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd



from .myplot import *
# import plotly.io as pio
# pio.renderers.default = "vscode"

# app = DjangoDash('SimpleExample')   # replaces dash.Dash

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

def reports(request):
    # session = request.session

    # demo_count = session.get('django_plotly_dash', {})

    # ind_use = demo_count.get('ind_use', 0)
    # ind_use += 1
    # demo_count['ind_use'] = ind_use
    # session['django_plotly_dash'] = demo_count

    # # Use some of the information during template rendering
    # context = {'ind_use' : ind_use}
    # print(context)


    reports = Report.objects.order_by('start_date')
    context = {"title": "Reports", "reports": reports}
    return render(request, 'reports/reports.html', context)





    # return render(request, 'reports/reports.html', context={'title': 'Reports'})

# if __name__ == '__main__':
# app.run(debug=True)s
    # context = {}
    # return render(request, 'reports/reports.html', context)