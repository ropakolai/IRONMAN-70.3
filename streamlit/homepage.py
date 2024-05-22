import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="Home",
    page_icon="/Users/Mac/Desktop/Projects/Regression/src/im.png"
)

# Sidebar image
st.sidebar.image("/Users/Mac/Desktop/Projects/Regression/src/ironman_logo.png")

# Sidebar pages
app_pages = ["Home", "Context", "Preprocessing", "Models", "Prediction", "Conclusion"]

# Selection in sidebar
page = st.sidebar.radio("Select a page:", app_pages)

# Home page function
def homepage():
    st.write("# IRONMAN 70.3 REGRESSION")

    st.write('''🏊‍♂️ This is a regression case that aims to estimate the finish time of a half ironman based on the age, 
    gender, and half-marathon time calculated with a known marathon average pace (as you don't run a half marathon alone as quickly
    as you run a half marathon after swimming and cycling).\n\n 🚴 The dataset consists of Ironman 70.3 race records around the world registered between 2010 and 2020, 
    including as main columns the tri-athletes gender, age group, country of origin, the year and the location of the race, 
    and the partial (swim, bike, run, transitions) and full race finish times (in seconds).  In total 795863 records from Ironman 70.3 PRO and recreational were used.
    Several models were tested: Linear Regression, Ridge Regression, Lasso Regression, Random Forest, Gradient Boosting, and XGBoost.\n\n🏃The best model was kept for prediction.\n\n Limits: no information on weather, elevation, number of supporters along the course, number of refueling sites on the course,
    and you have elites and amateurs athletes mixed in the dataset.''')

    st.markdown(
    """
    ### 
    - Dataset available at [kaggle](https://www.kaggle.com/datasets/aiaiaidavid/ironman-703-race-data-between-2004-and-2020/code)
    """
    )

    st.markdown(
    """
    ### IRONMAN 70.3 races locations
    
    - Web scraped from [locations](https://www.ironman.com/im703-races)
    """
    )
    
    # List of countries to color in red
    red_countries = ['Egypt', 'Morocco', 'Rwanda', 'South Africa', 'Bahrain', 'Dubai', 'India', 'Israel', 'Japan', 'Kazakhstan', 'Korea', 'Malaysia', 'Oman', 'Philippines',
                 'Taiwan', 'Thailand', 'Viet Nam', 'Austria', 'Belgium', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Ireland',
                 'Italy', 'Luxembourg', 'Netherlands', 'Poland', 'Portugal', 'Serbia', 'Spain', 'Sweden', 'Switzerland', 'Türkiye', 'United Kingdom', 'Canada', 'Mexico', 'Panama',
                 'Puerto Rico', 'United States of America', 'Australia', 'New Zealand', 'Argentina', 'Brazil', 'Chile', 'Colombia', 'Dominican Republic', 'Ecuador', 'Perú',
                 'Uruguay']

    # ISO-3166-1 alpha-3 codes of the countries
    iso_codes = ['EGY', 'MAR', 'RWA', 'ZAF', 'BHR', 'ARE', 'IND', 'ISR', 'JPN', 'KAZ', 'KOR', 'MYS', 'OMN', 'PHL',
             'TWN', 'THA', 'VNM', 'AUT', 'BEL', 'HRV', 'CZE', 'DNK', 'EST', 'FIN', 'FRA', 'DEU', 'GRC', 'IRL',
             'ITA', 'LUX', 'NLD', 'POL', 'PRT', 'SRB', 'ESP', 'SWE', 'CHE', 'TUR', 'GBR', 'CAN', 'MEX', 'PAN',
             'PRI', 'USA', 'AUS', 'NZL', 'ARG', 'BRA', 'CHL', 'COL', 'DOM', 'ECU', 'PER', 'URY']

    # Create the map
    fig = go.Figure()

    # Add a layer to the map
    fig.add_trace(go.Choropleth(
        locations=iso_codes,  # ISO-3166-1 alpha-3 codes
        z=[1]*len(iso_codes),  # Values for color
        colorscale=[[0, 'grey'], [1, 'red']],  # Color scale
        showscale=False,  # Hide color scale
        geo='geo',
    ))

    # Map parameters
    fig.update_geos(
        showcountries=True,  # Show borders between countries
        countrycolor='black', # Borders color
        oceancolor='black', # Oceans color
        projection_type='natural earth',  # Use default projection
        showocean=True,  # Be sure that oceans are shown
        lakecolor='black',# Lakes color
        bgcolor='black',
    )

    # Ad Mapbox layaout
    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=True,
            coastlinecolor='black',
            showland=True,
            landcolor='white',
            showocean=True,
            oceancolor='black'
        ),
        mapbox_style="carto-positron",  #  Mapbox style
        mapbox_zoom=1,  # Initial zoom level
        mapbox_center={"lat": 0, "lon": 0},  # Center of the map
    )

    # Show the map
    st.plotly_chart(fig,use_container_width=True)




# Import functions of other pafes
from utils.context import context_page
from utils.preprocessing import preprocessing_page
from utils.models import models_page
from utils.prediction import prediction_page
from utils.conclusion import conclusion_page

# Navigation through pages
if page == "Home":
    homepage()
elif page == "Context":
    context_page()
elif page == "Preprocessing":
    preprocessing_page()
elif page == "Models":
    models_page()
elif page == "Prediction":
    prediction_page()
elif page == "Conclusion":
    conclusion_page()
