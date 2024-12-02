# ## Challenge 6-1-1

# Using the `data/mobile_user_behavior_dataset.csv` file, create a streamlit to show:

# 1. the data in a dataframe 
# 2. select a category: gender or operating system
# 3. select a measure: Data useage, battery drain, screen on time, or app useage time
# 4. show a bar plot of the average of 3. by 2.

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#1
behavior = pd.read_csv("./6-viz/data/mobile_user_behavior_dataset.csv")


#2 
category = st.selectbox("Select System:", ["Operating System", "Gender"])
plot, series = plt.subplots()



#3
measure = st.selectbox("Select Measure:", ["Data Usage (MB/day)", "Battery Drain (mAh/day)", "Screen On Time (hour/day)", "App Usage Time (min/day)"])


sns.barplot(data=behavior, x= category, y="Data Usage (MB/day)", estimator="mean", errorbar = None, ax=series).set_title("Average Data Useage by Operating System")

#4

st.pyplot(plot)







