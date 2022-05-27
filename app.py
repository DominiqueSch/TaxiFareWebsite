import streamlit as st
import requests

st.markdown("""# Taxi Fare Model
## Predict taxi fares
Challenge to create a website for taxi fares in NYC""")

input_date_and_time = st.text_input('Insert date and time')
input_pickup_longitude = st.text_input('Insert pickup longitude')
input_pickup_latitude = st.text_input('Insert pickup latitude')
input_dropoff_longitude = st.text_input('Insert dropoff longitude')
input_dropoff_latitude = st.text_input('Insert dropoff latitude')
input_passenger_count = st.text_input('Insert passenger count')


url = 'https://taxifare.lewagon.ai/predict'


params = dict(
  pickup_datetime=input_date_and_time,
  pickup_longitude=input_pickup_longitude,
  pickup_latitude=input_pickup_latitude,
  dropoff_longitude=input_dropoff_longitude,
  dropoff_latitude=input_dropoff_latitude,
  passenger_count=input_passenger_count
)

response = requests.get(
    url,
    params=params
)

if response.status_code == 200:
    print("API call success")
else:
    print("API call error")

response.json().get("fare", "no prediction"), response.json()
