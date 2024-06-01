import streamlit as st
import requests
import datetime
import pandas as pd

date = st.date_input("Date", datetime.date.today())
time = st.time_input("Time", datetime.datetime.now())
date_and_time = str(datetime.datetime.combine(date, time))

pickup_longitude = st.number_input('Pickup Longitude', value=-73.985428)
pickup_latitude = st.number_input('Pickup Latitude', value=40.748817)
dropoff_longitude = st.number_input('Dropoff Longitude', value=-73.977233)
dropoff_latitude = st.number_input('Dropoff Latitude', value=40.752726)

passenger_count = st.number_input('Insert passenger count', 0)


url = 'https://taxifare.lewagon.ai/predict'


params = {
'pickup_datetime': date_and_time,
'pickup_longitude': pickup_longitude,
'pickup_latitude': pickup_latitude,
'dropoff_longitude': dropoff_longitude,
'dropoff_latitude': dropoff_latitude,
'passenger_count': passenger_count
}

response = requests.get(url, params=params)

if st.button('Get prediction'):
    st.write(round(response.json()['fare'], 2))

st.map(pd.DataFrame({'lat': [pickup_latitude,dropoff_latitude], 'lon': [pickup_longitude,dropoff_longitude]}, columns=['lat', 'lon']))
