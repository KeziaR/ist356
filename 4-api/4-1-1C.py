import streamlit as st
import pandas as pd
import requests

st.title("Dataframe For Data API")

# url = "https://jsonplaceholder.typicode.com/users/"
# reponse = requests.get(url)
# reponse.raise_for_status()
# read = reponse.json()

# users = pd.json_normalize(read)
# st.dataframe(read)

customers = pd.read_json("https://jsonplaceholder.typicode.com/users/")
st.dataframe(customers)