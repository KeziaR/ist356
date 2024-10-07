import streamlit as st
import pandas as pd
import requests

link = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees.json"
response = requests.get(link)
data = response.json()
df = pd.json_normalize(data, record_path='employees')
st.dataframe(df)


"""json_data = [
    { 

    }
]"""