import pandas as pd 
import streamlit as st


## Challenge 3-5-2

# https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv

# Let's build an interactive pivot table in streamlit!

# - create a row and column selection widgets allowing the user to select one of the following columns:  
# `'Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade'`
# - create a measure column selestion widget which allows the user to select one of these columns:  
# `'Completion_Time','Student_Score'`
# - build the pivot table dataframe from the inputs. use the average for the `aggfunc`
# - display the pivot table!

# **EXTRA CHALLENGE:** Do not allow the name value in row and column!


st.title("3-5-2 Challenge")

# loading in the data file

exam_scores = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv")
visual = st.dataframe(exam_scores)


# selection widgets for certain columns

user_select = st.selectbox('Select any of the following columns:' ,options = ['Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade'])
slected_widget = st.dataframe([exam_scores)

# Selecting the following columns to get its data by using grouping

exam_data = exam_scores.groupby(user_select)
exam_data

