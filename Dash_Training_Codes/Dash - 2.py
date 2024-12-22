# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:14:46 2024

@author: 10450
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:29:12 2024

@author: 10450
"""
#Import Packages
from dash import Dash, html,dash_table,dcc,callback,Output,Input
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

#We import dcc like we did in the previous section to use dcc.Graph. 
#In this example, we need dcc for dcc.Graph as well as the radio buttons component, 
#dcc.RadioItems.
#To work with the callback in a Dash app, we import the callback module 
#and the two arguments commonly used within the callback: Output and Input.

#Controls and Callbacks as our 3rd component we will add buttons and their
#usage

#1) The order you give the input determines the order it appears in the window,
#First we create radiobuttons after title as 2nd component then table then
#we tell we will give a graph using dcc.graph but figure is empty but it has an id
app.layout = [html.Div(children='First App with Data'),
              html.Hr(),
              dcc.RadioItems(options=[5,10,15,20,25],value=5,id="controls-radio"),
              dash_table.DataTable(data=data.to_dict("records"),page_size=10),
              dcc.Graph(figure={}, id='controls-radio-graph')
   
                        
              
              
              ]

# Add controls to build the interaction
#Here the output is the graph so its id is the same with dcc graph
#Input is the radiobutton value so the id is radiobutton id
@callback(
    Output(component_id='controls-radio-graph', component_property='figure'),
    Input(component_id='controls-radio', component_property='Temp')
)
                        
def update_graph(col_chosen):
    fig = px.line(data["Temp"],x=data["Temp"].index,
                                       y=data["Temp"])
    return fig

#Run the app
if __name__ == '__main__':
    app.run(debug=True,port=8050)