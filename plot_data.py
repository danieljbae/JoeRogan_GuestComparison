import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html


def create_dashboard(df):
    # Create plotly figure 
    years = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]

    print(df.head())
    fig_dict = {
        "data": [],
        "layout": {},
        "frames": []
    }

    ##################################################
    # make layout
    x_min = -1
    x_max = 10
    
    # x_min = df.loc[df['appearences_rollingCount'].idxmin()]['appearences_rollingCount']
    # x_max = df.loc[df['appearences_rollingCount'].idxmax()]['appearences_rollingCount']-30
    fig_dict["layout"]["xaxis"] = {"range": [x_min, x_max+5], "title": "# of Appearences"}
    fig_dict["layout"]["yaxis"] = {"title": "Average Number of Views (rolling)", "type": "log"}
    fig_dict["layout"]["hovermode"] = "closest"
    
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

    ##################################################
    # make data
    year = 2013 # 1st JRE episode

    df_by_year = df[df["upload_Year"] == year]
    data_dict = {
        "x": list(df_by_year["appearences_rollingCount"]),
        "y": list(df_by_year["views_rollingAvg"]),
        "mode": "markers",
        "text": list(df_by_year["guest_Names"]),
        "marker": {
            "sizemode": "area",
            "sizeref": 2.*max(df_by_year["engagementFactor_rollingAvg"])/(40.**2),
            "size": list(df_by_year["engagementFactor_rollingAvg"]),
            "sizemin": 4
        },
    }
    fig_dict["data"].append(data_dict)



    ##################################################
    # make frames
    for year in years:
        frame = {"data": [], "name": str(year)}
        df_by_year = df[df["upload_Year"] == int(year)]

        data_dict = {
            "x": list(df_by_year["appearences_rollingCount"]),
            "y": list(df_by_year["views_rollingAvg"]),
            "mode": "markers",
            "text": list(df_by_year["guest_Names"]),
            "marker": {
                "sizemode": "area",
                "sizeref": 2.*max(df_by_year["engagementFactor_rollingAvg"])/(40.**2),
                "size": list(df_by_year["engagementFactor_rollingAvg"]),
                "sizemin": 4
            },
            "name": year
        }
        frame["data"].append(data_dict)


        fig_dict["frames"].append(frame)
        slider_step = {"args": [
            [year],
            {"frame": {"duration": 300, "redraw": False},
            "mode": "immediate",
            "transition": {"duration": 300}}
        ],
            "label": year,
            "method": "animate"}
        sliders_dict["steps"].append(slider_step)


    fig_dict["layout"]["sliders"] = [sliders_dict]

    fig = go.Figure(fig_dict)
    fig.update_layout(template="plotly_dark")
    
    fig.show()



    ########### Dash - Dashboard ###########
    # app = dash.Dash()
    # app.layout = html.Div([
    #     dcc.Graph(figure=fig)
    # ])
    # app.run_server(debug=True)  # Turn off reloader if inside Jupyter

    
