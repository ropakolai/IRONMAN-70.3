import streamlit as st

def preprocessing_page():
    st.write("# 🏗 Preprocessing Pipeline 🏗")
    st.write("")
    st.write("The preprocessing pipeline was designed to prepare data for machine learning by applying appropriate transformations to different types of features (numeric and categorical) in the dataset.\n\n This is accomplished using the ColumnTransformer from scikit-learn, which allows us to apply different preprocessing steps to different subsets of the features.\n\n")
    st.write("By using this preprocessing pipeline, we ensure that:\n")
    st.write("📊 Numeric features ('RunTime', 'AgeBand') are standardized, making them suitable for models that assume features to be normally distributed.\n\n"
    " 🗂 Categorical features ('Gender') are converted into a binary format, making them compatible with algorithms that require numerical input.\n\n"
    "This structured approach to preprocessing allows a clean and efficient preparation of data before it is fed into a machine learning model.\n\n")
    st.image('/Users/Mac/Desktop/Projects/Regression/src/swim.jpeg')

# Call the function to run the Streamlit app
preprocessing_page()
