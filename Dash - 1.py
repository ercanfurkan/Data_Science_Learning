# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:29:12 2024

@author: 10450
"""
#Import Packages
from dash import Dash, html,dash_table,dcc
import pandas as pd
import plotly.express as px

#I guess we are creating a DASH object

app = Dash()

#App Layout
#App components that will be displayed in browser


#Add data
data = pd.read_csv("C:\\Users\\10450\\Desktop\\Sürastarya Weather Derivative\\Weather Derivatives\\2023 HP iskelesi verileri.csv",
                  delim_whitespace=True)
data = data.reset_index()

#App layout takes list
#The 2nd component is a table representation of the Data
#The dash_table module gives this property
#It is DataTable provided by dash_table
#The first component is the title
#We import dcc module (Dash Core Componenents) we use dcc.graph to make graphs
#Also then we use plotly.express to give it as a figure input
#This is our 3rd component,title,table,graph

#Controls and Callbacks as our 4th component we will add buttons and their
#usage

app.layout = [html.Div(children='First App with Data'),
              dash_table.DataTable(data=data.to_dict("records"),page_size=10),
              dcc.Graph(figure=px.line(data["Temp"],x=data["Temp"].index,
                                       y=data["Temp"])
                        )
                        
                        
              
              
              ]


#Run the app
if __name__ == '__main__':
    app.run(debug=True,port=8050)