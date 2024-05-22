import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import json


def context_page():
    st.write("# Context")
    st.write("As part of my endurance sports journey, I participated to a marathon. It went pretty well and I enjoyed the whole process. As every athlete, I've come to ask myself : What's the next challenge? As you guys probably have guessed, I aim to participate to a half IRONMAN (70.3 miles), which consists to do:\n\n"
             "🏊 a 1.2-mile (1.9 km) swim\n\n"
             "🚴 a 56-mile (90 km) bike ride\n\n"
             "🏃 a 13.1-mile (21.1km) run \n\n"
             "Having as my only reference my time and my average marathon pace, I told myself that with enough data and machine learning I could have an estimate of the time I can aim to complete an IRONMAN 70.3\n\n")
    st.write("As describe in the home page, I used 795863 IRONMAN 70.3 records from around the world between 2010 and 2020.")
    st.write("## A few insights about the dataset\n\n")
    


    def load_plotly_figure(filepath):
        with open(filepath, "r") as f:
            fig_json = json.load(f)
        fig = go.Figure(fig_json)
        return fig

    def load_dataframe(filepath):
        df = pd.read_json(filepath)
        return df

    # Load the pre-generated Plotly figures
    fig1 = load_plotly_figure("/Users/Mac/Desktop/Projects/Regression/src/plotly_figure1.json")
    fig2 = load_plotly_figure("/Users/Mac/Desktop/Projects/Regression/src/plotly_figure2.json")
    fig3 = load_plotly_figure("/Users/Mac/Desktop/Projects/Regression/src/plotly_figure3.json")
    
    # Display the figures in Streamlit
    st.plotly_chart(fig1)

    st.plotly_chart(fig2)

    # Load and display the JSON table
    st.write("### Stats Table")
    json_df = load_dataframe("/Users/Mac/Desktop/Projects/Regression/src/table.json")
    st.write(json_df)
    
    st.plotly_chart(fig3)

    

# Call the function to run the Streamlit app
context_page()


