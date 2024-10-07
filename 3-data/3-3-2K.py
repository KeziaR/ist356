import streamlit as st
import pandas as pd
import requests

base = "https://raw.githubusercontent.com/mafudge/datasets/master/minimart/"

Customers = pd.read_csv(base + '/customers.csv')
march = pd.read_csv(base + '/march.csv')
mons = ['jan', 'feb', 'mar', 'apr']
months_df =[]
for month in mons:
    months_df = pd.read.csv(base + f'/purchase-{month}.csv')
    months_df['month'] = month
    months_df.append(months_df)

purchases = pd.concat(months_df)
combined = pd.merge(Customers, purchases, on='customer_id', how="left")
st.write("Combined Data")
select_month = st.selectbox("Select a month", mons)
filtered = combined[combined['month'] == select_month]
no_purchase = combined[combined['order_id'].isnull()]
st.dataframe(no_purchase)
