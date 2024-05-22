import streamlit as st

def conclusion_page():
    st.write("# 🏁 Conclusion 🏁")
    st.write("""
    This project obviously has biases. We do not have weather data which can greatly affect performance, the elevation of the course, the number of supporters per event, the distance to be covered during transition times, and the number of refueling sites.\n Additionally, in the dataset we have mixed professional and amateur athletes.\n\n Finally, it is obvious that predicting a time for a triathlon is not easy, especially when using only age, gender, and average marathon pace. However, this model allows us to obtain an estimate, or even an objective (for my case), and it must be emphasized that this entire project was carried out mainly out of curiosity.
    \n\n""")
    st.write("")
    st.image("src/images/finish.jpeg")

conclusion_page()
