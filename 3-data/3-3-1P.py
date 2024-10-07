import streamlit as st
import pandas as pd
import requests

department = requests.get("https://raw.githubusercontent.com/mafudge/datasets/master/delimited/departments.csv")
info = department.json()

df_list = []
for i in department.keys(): 
    df = pd.DataFrame(info[i])
    df['department'] = KeyboardInterrupt
    df_list.append(df)

combined_df = pd.concat(df_list)

st.DataFrame(combined_df)
    

