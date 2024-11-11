import requests
import streamlit as st

#geocode
st.title("Data API Example")
loc = st.text_input("Enter a location")
weather = st.text_input("Enter weather")

'''curl -X 'GET' \
  'https://cent.ischool-iot.net/api/google/geocode?location=syracuse' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: b3f5c4ac2282aa161f938c47'''

#weather
'''curl -X 'GET' \
  'https://cent.ischool-iot.net/api/weather/current?units=metric&lon=43&lat=45' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: b3f5c4ac2282aa161f938c47'''

if st.button("Get Geocode"):
    url = "https://cent.ischool-iot.net/api/google/geocode"
    querystring = {"location":loc}
    response = requests.get(url, params=querystring, headers={"X-API-KEY":"b3f5c4ac2282aa161f938c47"})      
    response.raise_for_status()
    geocode = response.json()
    st.write(geocode)
if st.button("Get Weather"):
    url = "https://cent.ischool-iot.net/api/google/weather/current"
    querystring = {"units": "imperial", "lon" : "lon", "lat" : "lat"}
    response = requests.get(url, params=querystring, headers={"X-API-KEY":"b3f5c4ac2282aa161f938c47"})      
    response.raise_for_status()
    weather = response.json()
    temp = weather['current']['tempurature_2m']
    
    st.write(weather)


