import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# The file is encoded using ISO-8859-1 character encoding, which is a standard way of representing characters in the file.
# We defined data type of specific columns such as (Div1Airport, Div1TailNum, Div2Airport, and Div2TailNum) to be strings, which ensures that these columns are read as text instead of numbers.
airline_data =  pd.read_csv('/Users/thuytrang/Documents/projects/dashboards-plotly/raw-data/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})
# Create a dash application layout
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add a html.Div and core input text component
# Finally, add graph component.
# Heading reference: Plotly H1 HTML Component
# Title as Airline Performance Dashboard
# Use style parameter for the title and make it center aligned, with color code #503D36, and font-size as 40.
app.layout = html.Div(children=[html.H1('Airline Performance Dashboard',style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
                                html.Div(["Input Year", dcc.Input(id='input-year', value='2010',
                                                                  type='number', style={'height':'50px', 'font-size': 35}),], 
                                style={'font-size': 40}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id='line-plot')),
                                ])
# Run the app
if __name__ == '__main__':
    app.run_server()