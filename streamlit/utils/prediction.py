import streamlit as st
import pandas as pd
import joblib
import sklearn

def prediction_page():
    st.write("# 🔮 Prediction 🔮")
    st.write("As said in the home page, this is a regression case that aims to estimate the finish time of a half ironman based on the age, gender, and half-marathon time calculated with a known marathon average pace (as you don't run a half marathon alone as quickly as you run a half marathon after swimming and cycling)")
    st.write("### How it works:")
    st.write("")
    st.image("src/images/model.png")

    # Load the best model
    best_model = joblib.load('model/ironman_model.pkl')  

    # Function to convert pace (min/km) to time in seconds and HH:MM:SS
    def convert_pace_to_total_time(pace_min_per_km):
        """
        Convertit une allure (min/km) en temps total pour un semi-marathon (21,1 km)

        Args:
        pace_min_per_km (float): Allure en minutes par kilomètre

        Returns:
        tuple: Temps total en secondes et formaté en HH:MM:SS
        """
        half_marathon_distance = 21.1
        total_time_minutes = pace_min_per_km * half_marathon_distance
        total_time_seconds = total_time_minutes * 60
        hours = int(total_time_seconds // 3600)
        minutes = int((total_time_seconds % 3600) // 60)
        seconds = int(total_time_seconds % 60)
        total_time_hhmmss = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        return total_time_seconds, total_time_hhmmss

    # Function to convert seconds to HH:MM:SS
    def time_in_HHMMSS(seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    # Streamlit app
    st.title('IRONMAN70.3 Time Predictor')

    # Get user inputs
    pace_min_per_km = st.number_input('Enter your average marathon pace (min/km):', min_value=0.0, step=0.01)
    age = st.number_input('Enter your age:', min_value=0, step=1)
    gender = st.selectbox('Select your gender:', options=['Male', 'Female'])

    # Convert gender to numerical value
    gender_num = 0 if gender == 'Male' else 1

    if st.button('Predict'):
        # Convert pace to total time
        total_seconds, total_hhmmss = convert_pace_to_total_time(pace_min_per_km)
    
        # Create input dataframe
        data_input = pd.DataFrame([[total_seconds, age, gender_num]], columns=['RunTime', 'AgeBand', 'Gender'])
    
        # Make prediction
        predicted_time_seconds = best_model['Pipeline'].predict(data_input)[0]
        predicted_time_hhmmss = time_in_HHMMSS(int(predicted_time_seconds))
    
        # Display the result
        st.write(f'Your predicted IRONMAN 70.3 time is: {predicted_time_hhmmss} !!!🏅')




# Call the function to run the Streamlit app
prediction_page()
