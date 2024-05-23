import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio


# Page config
st.set_page_config(
    page_title="Home",
    page_icon="src/images/im.png"
)

# Read URL parameters
query_params = st.experimental_get_query_params()
page = query_params.get('page', ['Home'])[0]

# Sidebar image
st.sidebar.image("src/images/ironman_logo.png")

# Sidebar pages
app_pages = ["Home", "Context", "Preprocessing", "Models", "Prediction", "Conclusion"]

# Selection in sidebar
page = st.sidebar.radio("Select a page:", app_pages,  index=app_pages.index(page))

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
    \n\n"""
    )

    # Load the figure from the JSON file
    file_name = "src/figures_table/halfironman_map.json"
    fig = pio.read_json(file_name)

    # Display the figure in Streamlit
    st.plotly_chart(fig, use_container_width=True)


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


# Custom CSS for positioning text
custom_css = """
<style>
.bottom-right {
    position: fixed;
    bottom: 10px;
    right: 20px;
    background-color: rgba(255, 255, 255, 0.8);
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
</style>
"""

# Custom HTML for the text
custom_html = """
<div class="bottom-right">
    © 2024 Nikolai ROPA
</div>
"""

# Injecting CSS and HTML into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(custom_html, unsafe_allow_html=True)

