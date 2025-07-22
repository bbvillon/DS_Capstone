# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Get unique launch sites for the dropdown options
launch_sites = spacex_df['Launch Site'].unique().tolist()

# Create options list for the dropdown, including 'All Sites'
dropdown_options = [{'label': 'All Sites', 'value': 'ALL'}]
for site in launch_sites:
    dropdown_options.append({'label': site, 'value': site})

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                dcc.Dropdown(id='site-dropdown',
                                            # Use the dynamically generated options list here
                                            options=dropdown_options,
                                            value='ALL',
                                            placeholder="Select a Launch Site here",
                                            searchable=True
                                            ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                dcc.RangeSlider(id='payload-slider',
                                                min=0, max=10000, step=1000,
                                                marks={0: '0', 2500: '2500', 5000: '5000',
                                                7500: '7500', 10000: '10000'},
                                                value=[min_payload, max_payload] # Initial value set to min and max payload
                                                ),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    """
    Generates a pie chart showing total success launches.
    If 'ALL' sites are selected, it shows success by launch site.
    If a specific site is selected, it shows success vs. failure for that site.
    """
    if entered_site == 'ALL':
        # Pie chart for all sites: values are 'class' (success/failure), names are 'Launch Site'
        fig = px.pie(spacex_df, values='class',
                     names='Launch Site',
                     title='Total Success Launches By Site')
        return fig
    else:
        # Filter data for the selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        # Calculate success (1) vs. failure (0) counts for the selected site
        # value_counts() returns a Series, reset_index() converts it to DataFrame
        success_counts = filtered_df['class'].value_counts().reset_index()
        success_counts.columns = ['class', 'count'] # Rename columns for clarity in plot

        # Create pie chart for success vs. failure
        fig = px.pie(success_counts,
                     values='count',
                     names='class',
                     title=f'Total Success Launches for site {entered_site}',
                     # Optional: Map class 1 to 'Success' and 0 to 'Failure' for better labels
                     # This makes the legend more descriptive
                     color='class',
                     color_discrete_map={0: 'red', 1: 'green'} # Assign colors for failure/success
                     )
        return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload-slider', component_property='value')])
def get_scatter_chart(entered_site, payload_range):
    """
    Generates a scatter plot showing correlation between payload and launch success.
    Filters data based on selected launch site and payload range.
    """
    # Extract min and max payload from the slider value
    low_payload, high_payload = payload_range

    # Filter the DataFrame based on the payload range first
    filtered_df_by_payload = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= low_payload) &
        (spacex_df['Payload Mass (kg)'] <= high_payload)
    ]

    if entered_site == 'ALL':
        # Scatter plot for all sites: x=Payload Mass, y=class, color by Booster Version Category
        fig = px.scatter(filtered_df_by_payload,
                         x='Payload Mass (kg)',
                         y='class',
                         color='Booster Version Category', # Color points by booster type
                         title='Correlation between Payload and Success for All Sites')
        return fig
    else:
        # Filter data for the selected site AND payload range
        filtered_df_site_payload = filtered_df_by_payload[
            filtered_df_by_payload['Launch Site'] == entered_site
        ]
        # Scatter plot for specific site: x=Payload Mass, y=class, color by Booster Version Category
        fig = px.scatter(filtered_df_site_payload,
                         x='Payload Mass (kg)',
                         y='class',
                         color='Booster Version Category', # Color points by booster type
                         title=f'Correlation between Payload and Success for site {entered_site}')
        return fig

# Run the app
if __name__ == '__main__':
    app.run()
