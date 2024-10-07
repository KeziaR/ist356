import streamlit as st
import pandas as pd
import checking

loading = requests.get("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv")
data = loading.json()

