import streamlit as st
import requests
from PIL import Image
import time

st.image("C:/Users/BHARGAV-RADADIYA/GenAi/FastAPI/br_logo.png", width=200)

st.title("Registration Open!")

with st.form("registration_form"):

    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")

    age = st.slider("Age", 0, 100)

    option = ["English", "Hindi", "Gujarati", "Tamil", "Japanese"]
    choice = st.multiselect("Languages Known:", option)

    address = st.text_area("Address")

    date = st.date_input("Birth Date")

    gender = st.radio("Gender", ("Male", "Female"))

    submit = st.form_submit_button("Submit")


if submit:
    if not first_name: 
        st.error("Please enter your First Name.") 
    elif not last_name: 
        st.error("Please enter your Last Name.") 
    elif not email: 
        st.error("Please enter your Email.") 
    elif not choice: 
        st.error("Please select at least one Language.") 
    elif not address: 
        st.error("Please enter your Address.")
    else:

        registration_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "age": age,
            "languages_known": choice,
            "address": address,
            "birth_date": str(date),
            "gender": gender
        }

        response = requests.post(
            "http://127.0.0.1:8000/register",
            json=registration_data
        )

        if response.status_code == 200:

            with st.spinner("Loading....."):
                time.sleep(2)

            st.success("Successfully Submitted!")
            st.snow()

        else:
            st.error("Registration failed!")