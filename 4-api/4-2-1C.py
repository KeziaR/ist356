import requests
import pandas as pd
import streamlit as st

st.title("Dataframe For KeyPhrases API")
def extract_keyphrases(text: str) -> dict:

    
    # curl -X 'POST' \
    # 'https://cent.ischool-iot.net/api/azure/keyphrasextraction' \
    # -H 'accept: application/json' \
    # -H 'X-API-KEY: b3f5c4ac2282aa161f938c47' \
    # -H 'Content-Type: application/x-www-form-urlencoded' \
    # -d 'text=The%20Dallas%20Cowboys%20are%20a%20far%20better%20team%20than%20the%20New%20York%20Giants%20this%20year.%20The%20Giants%20have%20not%20won%20a%20conference%20game%20yet.'
    


    url = 'https://cent.ischool-iot.net/api/azure/keyphrasextraction'
    data = {'text': text}
    headers = {
        'X-API-KEY': 'b3f5c4ac2282aa161f938c47',
    }

    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.json

text = st.text_input("Enter text")
if text:
    results = extract_keyphrases(text)
    extract = results['results']['documents'][0]['extract']
   

    # input data into a dataframe  
    
    phrases = pd.DataFrame(extract)
    st.dataframe(phrases)