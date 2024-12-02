# ## Challenge 6-1-2

# Write a streamlit to load the `data/mobile_user_behavior_dataset.csv` file, and display the conrents.

# which columns are be used the x-axis of a line plot?

# Create a plot to show the relationship between someone's age and their data usage.

# Create another plot to show the relationship between someone's age and gender and their data usage.

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#1
mobile = pd.read_csv("./6-viz/data/mobile_user_behavior_dataset.csv")
st.dataframe(mobile)

figure, series = plt.subplot()
sns.lineplot(data=mobile,
             x="Age",
             y="Number of Apps Installed",
             estimator="mean",
             errorbar= None,
             ax=series)
st.pyplot(figure)








