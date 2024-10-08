import streamlit as st
import requests

st.title("FastTrack Promotions: Leveraging AI for Smarter HR Decisions")
tab1,tab2=st.tabs([' 🏡 Home ',' Predict Promotion Status '])
with tab1:
    st.header(" 👤 Welcome User")
    st.subheader("Promotion Prediction")
    st.write("In modern organizations, employee promotions play a crucial role in career advancement and workforce development. However, determining which employees are most suitable for promotion can be a challenging task. To tackle this issue, we have developed an Employee Promotion Prediction system using machine learning, which leverages key employee data to predict whether an individual is likely to be promoted.")
    st.subheader("API Development with FastAPI")
    st.write("To make the prediction model easily accessible, we created a RESTful API using FastAPI, a modern, high-performance web framework for building APIs. This API exposes a /predict endpoint that accepts employee data as input and returns a prediction on whether the employee will be promoted. The API is powered by Uvicorn, a fast ASGI server, ensuring it can handle multiple requests efficiently and serve predictions quickly.")
with tab2:
    Id=st.number_input(label = "Employee Id", step=1, format="%i")
    tr=st.number_input(label = "No. of trainings", step=1, format="%i")
    age=st.number_input(label = "Age", step=1, format="%i")
    pyr=st.number_input(label = "Previous Year Rating", step=1., format="%.2f")
    los=st.number_input(label = "Length of service" , step=1, format="%i")
    aw=st.number_input(label = "Awards won" , step=1, format="%i")
    avg=st.number_input(label = "Average training score", step=1., format="%.2f")
    
    base_url = "http://localhost:8000"
   
    data = {
    "employee_id": Id,
    "no_of_trainings": tr,
    "age": age,
    "previous_year_rating": pyr,
    "length_of_service": los,
    "awards_won": aw,
    "avg_training_score": avg
    }
    
    if st.button("Predict"):
        response = requests.post(f"{base_url}/predict", json=data)
        if response.status_code == 200:
            st.write(response.json()) 
        else:
            st.write(f"Request failed with status code: {response.status_code}")

    
