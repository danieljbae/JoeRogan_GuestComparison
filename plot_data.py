import plotly.express as px
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html

from datetime import datetime, timedelta
from collections import OrderedDict
import math
from pandas import DataFrame
import sqlite3
import pandas as pd

def create_dashboard(db_filename,table_name,dfcolumn_names):

    ########################################
    # Load data from database into df 
    ########################################
        
    # use data from db file
    conn = sqlite3.connect(db_filename) 
    c = conn.cursor()

    # Load data 
    c.execute(f'''  
    SELECT * FROM {table_name}
            ''')

    df = DataFrame(c.fetchall(), columns=dfcolumn_names)    
    print (df.head())



    ########################################
    # Create plotly figure (bubble chart) 
    ######################################## 
    start = "2013-01-01"  # first show 
    end = "2020-10-01" 
    dates = [start, end]
    start, end = [datetime.strptime(_, "%Y-%m-%d") for _ in dates]
    month_years = list(OrderedDict(((start + timedelta(_)).strftime(r"%Y-%m"), None) for _ in range((end - start).days)).keys())

    fig_dict = {
        "data": [],
        "layout": {},
        "frames": []
    }

    ### Make layout of plot
    x_min = 0
    x_max = math.log(50,10)

    y_min = 0
    y_max = math.log(100000000,10) 

    fig_dict["layout"]["yaxis"] = {"range":[y_min,y_max],"title": "Total Number of Views (rolling)", "type": "log"}
    fig_dict["layout"]["xaxis"] = {"autorange":True,"title": "# of Appearences", "type": "log"}
    fig_dict["layout"]["hovermode"] = "closest"
    fig_dict["layout"]["dragmode"]='pan'
    
    fig_dict["layout"]["updatemenus"] = [
        {
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 500, "redraw": False},
                                    "fromcurrent": True, "transition": {"duration": 300,
                                                                        "easing": "quadratic-in-out"}}],
                    "label": "Play",
                    "method": "animate"
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                    "mode": "immediate",
                                    "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate"
                }
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top"
        }
    ]


    sliders_dict = {
    "active": 0,
    "yanchor": "top",
    "xanchor": "left",
    "currentvalue": {
        "font": {"size": 20},
        "prefix": "Year:",
        "visible": True,
        "xanchor": "right"
    },
    "transition": {"duration": 300, "easing": "cubic-in-out"},
    "pad": {"b": 10, "t": 50},
    "len": 0.9,
    "x": 0.1,
    "y": 0,
    "steps": []
    }

    
    ### Set up data of plot
    month_year  = "2013-01" # 1st JRE episode

    df_by_year = df[df["upload_month_year"] == month_year]
    data_dict = {
        "x": list(df_by_year["appearences_rollingCount"]),
        "y": list(df_by_year["views_rollingSum"]),
        "mode": "markers",
        "text": list(df_by_year["guestName_show"]),
        
        ### Bubble parameters (size and color)
        "marker": {
            "color": df_by_year['contraversyFactor'],
            "colorscale": "rdylgn",   
            "showscale":True,
            "sizemode": "area",
            "sizeref": 2*2.*max(df_by_year["engagementFactor_rollingAvg"])/(40.**2),
            "size": list(df_by_year["engagementFactor_rollingAvg"]),
            "sizemin": 4
        },
    }
    fig_dict["data"].append(data_dict)


 
    ### Make frames per time period (to animate)
    for month_year in month_years:
        frame = {"data": [], "name": str(month_year)}
        df_by_year = df[df["upload_month_year"] == month_year]

        data_dict = {
            "x": list(df_by_year["appearences_rollingCount"]),
            "y": list(df_by_year["views_rollingSum"]),
            "mode": "markers",
            "text": list(df_by_year["guestName_show"]),
            "marker": {
                "color": df_by_year['contraversyFactor'],
                "colorscale": "rdylgn",   
                "showscale":True,
                "sizemode": "area",
                "sizeref": 2*2.*max(df_by_year["engagementFactor_rollingAvg"])/(40.**2),
                "size": list(df_by_year["engagementFactor_rollingAvg"]),
                "sizemin": 4
            },
            "name": month_year
        }
        frame["data"].append(data_dict)


        fig_dict["frames"].append(frame)
        slider_step = {"args": [
            [month_year],
            {"frame": {"duration": 300, "redraw": False},
            "mode": "immediate",
            "transition": {"duration": 300}}
        ],
            "label": month_year,
            "method": "animate"}
        sliders_dict["steps"].append(slider_step)



    fig_dict["layout"]["sliders"] = [sliders_dict]
    

    fig = go.Figure(fig_dict)
    fig.update_layout(template="plotly_dark")
    # fig.show()



    ########################################
    # Design Dashboard
    ########################################

    # app = dash.Dash()

    # ### Basic Graph dataframe plotting 
    # # HTML Components 
    # app.layout = html.Div(children = [
    #     html.H1("Joe Rogan Podcast Guests Comparison"),
    #     dcc.Graph(
            
    #         id='Example',
    #         figure = fig
    #     )   
            
    # ])


    # app.run_server(debug=True)




    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    # # assume you have a "long-form" data frame
    # # see https://plotly.com/python/px-arguments/ for more options
    # # df = pd.DataFrame({
    # #     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    # #     "Amount": [4, 1, 2, 2, 4, 5],
    # #     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    # # })

    # # fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

    #     html.Div(children='''
    #         Dash: A web application framework for Python.
            
            
    #     '''),
    #     html.H1(children='Hello world'),
    #     html.P(children = 'okay this is nice'),


    #     html.Div(className="container",
        
        
    #     children=[
        
    #         html.Div(className=""


    #         )

    #     ])

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])

# if __name__ == '__main__':
    app.run_server(debug=True)