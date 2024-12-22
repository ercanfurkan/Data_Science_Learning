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
import numpy as np
import plotly.express as px

#I guess we are creating a DASH object

app = Dash()

#App Layout
#App components that will be displayed in browser


#Add data---------------
data = pd.read_csv("C:\\Users\\10450\\Desktop\\Sürastarya Weather Derivative\\Weather Derivatives\\2023 HP iskelesi verileri.csv",
                  delim_whitespace=True)
data.drop("Date",axis=0,inplace=True)
data = data.reset_index()

#Data Cleaning----------
#Arrange Col Names
column_names = data.columns.values
column_names[0] = "Date"
column_names[1] = "Time"
column_names[2] =  "Out Temp"
column_names[3] =  "High Temp"
column_names[4] =  "Low Temp"
column_names[5] =  "Humidity Out"
column_names[6] = "Dew Pt"
column_names[7] = "Wind Speed"
column_names[8] = "Wind Dir"
column_names[9] = "Wind Run"
column_names[10] = "High Speed"
column_names[11] = "High Direction"
column_names[12] = "Wind Chill"
column_names[13] = "Heat Index"
column_names[14] = "THW Index"
column_names[15] = "Bar"
column_names[16] = "Rain"
column_names[17] = "Rain Rate"
column_names[18] = "Heat D-D"
column_names[19] = "Cool D-D"
column_names[20] = "In Temp"
column_names[21] = "In Humidity"
column_names[22] = "In Dew"
column_names[23] = "In Heat"
column_names[24] = "In Emc"
column_names[25] = "In Air Density"
column_names[26] = "Wind Samp"
column_names[27] = "Wind Tx"
column_names[28] = "ISS Recept"
column_names[29] = "Arc. Int."
data.columns = column_names
#Arrange Date Times
data["DateTime"] = data["Date"] + " " + data["Time"]
data["DateTime"] = pd.to_datetime(data["DateTime"])
data.index = data["DateTime"]
data.drop("DateTime",axis=1,inplace=True)
#Arrange '---' values to NaN
data["Out Temp"] = data["Out Temp"].replace('---',np.nan)
data["High Temp"] = data["High Temp"].replace('---',np.nan)
data["Low Temp"] = data["Low Temp"].replace('---',np.nan)
data["Humidity Out"] = data["Humidity Out"].replace('---',np.nan)
data["Dew Pt"] = data["Dew Pt"].replace('---',np.nan)
data["Wind Dir"] = data["Wind Dir"].replace('---',np.nan)
data["High Direction"] = data["High Direction"].replace('---',np.nan)
data["Wind Chill"] = data["Wind Chill"].replace('---',np.nan)
data["Heat Index"] = data["Heat Index"].replace('---',np.nan)
data["THW Index"] = data["THW Index"].replace('---',np.nan)
#Convert ederken buldum
data["Bar"] = data["Bar"].replace('------',np.nan)
#Bir satırı --1396 full boş çekmiş glb
data["Heat D-D"] = data["Heat D-D"].replace('---',np.nan)
data["Cool D-D"] = data["Cool D-D"].replace('---',np.nan)
data["In Temp"] = data["In Temp"].replace('---',np.nan)
data["In Humidity"] = data["In Humidity"].replace('---',np.nan)
data["In Dew"] = data["In Dew"].replace('---',np.nan)
data["In Heat"] = data["In Heat"].replace('---',np.nan)
data["In Emc"] = data["In Emc"].replace('---',np.nan)
data["In Air Density"] = data["In Air Density"].replace('---',np.nan)
#Wind Speed lots of 0s about the number of --- in other columns is it Null ??
#Similar in wind Run  and High speed too
#In Bar seems to be no nulls but in Rain 32k 0s probably nulls same with Rain Rate as well
#In heat D-D 22k 0s, Cool D-D 18k 0s
#In temp seems ok In Humiditiy seems ok In Dew Seems Ok In Heat Seems Ok
#In Emc seems OK In air density seems ok
# wind samp has 6k 0s
#Wind Tx mosts all 2 or 1
#ISS Recept 32k 100
#Arc Int All 10
#Convert All Values to Numerics
#Wind Dir and High Dir are exceptions
for i in range(2,8):
    #Take the column name
    col_name = data.iloc[:,i].reset_index().columns[1]
    data[col_name] = pd.to_numeric(data.iloc[:,i])
for i in range(9,10):
    #Take the column name
    col_name = data.iloc[:,i].reset_index().columns[1]
    data[col_name] = pd.to_numeric(data.iloc[:,i])
for i in range(12,30):
    #Take the column name
    col_name = data.iloc[:,i].reset_index().columns[1]
    #print(i)
    data[col_name] = pd.to_numeric(data.iloc[:,i])
    
    
#Data Cleaning Ends------------

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
              dcc.RadioItems(options=[5,10,15,20,25,50,100],value=10,id="controls-radio"),
              dash_table.DataTable(data=data.to_dict("records"),page_size=10),
              dcc.Graph(figure={}, id='controls-radio-graph')
   
                        
              
              
              ]

# Add controls to build the interaction
#Here the output is the graph so its id is the same with dcc graph
#Input is the radiobutton value so the id is radiobutton id
@callback(
    Output(component_id='controls-radio-graph', component_property='figure'),
    Input(component_id='controls-radio', component_property='value')
)
                        
def update_graph(col_chosen):
    fig = px.line(data["Out Temp"],x=data[0:col_chosen]["Out Temp"].index,
                                       y=data[0:col_chosen]["Out Temp"]
                                       )
    return fig

#Run the app
if __name__ == '__main__':
    app.run(debug=True,port=8050)
