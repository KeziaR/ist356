import pandas as pd 
import streamlit as st


# https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv

# Create a streamlit to allow the user to select one of the following:

# - one of: Made_Own_Study_Guide, Did_Exam_Prep Assignment, Studied_In_Groups	

# - after the selection is made display a dataframe that summarized the count 
# of students and the average student score by the selection

st.title("3-5-1 Challenge")

# Allowing loading data from csv file and displaying data in dataframe 
# for clear understanding of data

data = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv")


#  creating a select option for users who Made_Own_Study_Guide,
#  Did_Exam_Prep Assignment, or Studied_In_Groups using streamlit	

Made_Own_Study_Guide = st.selectbox('Study Types', options=['Made_Own_Study_Guide','Did_Exam_Prep Assignment','Studied_In_Groups'])

# grouping the type of studying into users who Made_Own_Study_Guide,
#  Did_Exam_Prep Assignment, or Studied_In_Groups

study_methods = data.groupby(Made_Own_Study_Guide)


study_df = st.dataframe([Made_Own_Study_Guide])

# A dataframe that shows the count of students per section and the average 
# student score by each study method
Selection2 = data.groupby(by=['Made_Own_Study_Guide' , 'Did_Exam_Prep Assignment' , 'Studied_In_Groups']).agg({'Class_Section': 'count', 'Student_Score': 'mean'} )
Selection2

