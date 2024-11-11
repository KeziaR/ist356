import pandas as pd
import requests 
import streamlit as st


# Let's write an LLM-based spellchecker!

# The spellchecker should take some text as input and return the misspelled 
# 
# works along with suggestions for the correct spellings. 

# Make the inputs, then create a suitable prompt for the LLM. 

def spellcheck(text):
    params = {"temperature" : 10 }
    api_key = "b3f5c4ac2282aa161f938c47"

    prompt = "Write a spellchecker that takes the following text and returns the misspelled words along with suggestions for the correct spellings:\n\n"
    prompt += text 

    uri = "https://cent.ischool-iot.net/api/openai/generate"
    headers = {"X-API-KEY": api_key}
    data = {
        "query": prompt
    }

    response = requests.post(uri, headers=headers, data=data, params = params)
    response.raise_for_status()
    results = response.json()
    return results

response = spellcheck("I am a good speler")
st.write(response)

def check_spelling(text):
    prompt = "Write a spellchecker that takes the following text and returns the misspelled words along with suggestions for the correct spellings:\n\n"
    prompt += text + "\n"
    prompt += "for each misspelled word, provide a suggestion for the correct spelling\n"
    response = spellcheck(prompt)
    return response


st.title("Spellchecker")
text = st.text_area("Enter some text")
response = check_spelling(text)
st.write(response)



    




