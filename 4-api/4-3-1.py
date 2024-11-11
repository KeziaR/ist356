
import requests
import streamlit as st

def get_text(query: str) -> str:

    url = "https://cent.ischool-iot.net/api/openai/generate"
    data = { "query": query }
    headers = {

        "X-API-KEY": 'b3f5c4ac2282aa161f938c47'

    }

    response = requests.post(url, data = data, headers = headers)
    response.raise_for_status()
    return response.json()                       


st.title("ChatGPT Practice")
text = st.text_area("Enter text")
if text: 
    with st.spinner("loading..."):
        response = get_text(text)
        st.write(response)