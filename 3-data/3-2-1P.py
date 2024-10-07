import streamlit as st
import pandas as pd

location = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log"

data = pd.read_csv(f'{location}', sep=" ", skiprows= 3, header = 0, names= ['time-taken', 'sc-status'])

##st.dataframe(data)

filtering = (data['time-taken'] > 500) & (data['sc-status'] == 200)
st.dataframe(data[filtering])

"""# initialize
if 'time' not in data.columns:
    st.write("Data not loaded")
if 'sc-status' not in data.columns:
    st.write("Data not loaded")

cols = st.number_input('Columns',)

if data == 'time':
    st.dataframe(locations.)
elif data == 'sc-status':
    st.dataframe(locations.)"""

