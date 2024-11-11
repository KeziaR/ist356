import pandas as pd
import streamlit as st

def grade(participation: float) -> str:
    if participation == 0.0:
        return "AB"
    
    if participation <= 0.5:
        return "np"
    
    return "+"

# Extract
# - reading data in
# - adding lineage

# extract roster
roster_url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/roster.csv"
roster_df = pd.read_csv(roster_url)
st.dataframe(roster_df)

#extract each poll
polls = []
dates = ['2024-01-08', '2024-01-15', '2024-01-22', '2024-01-29']

for date in dates:
    poll = f"https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/poll-responses-{date}.csv"
    poll_df = pd.read_csv(poll)
    # add lineage
    poll_df['date'] = date
    # add poll to list
    polls.append(poll_df)

polls_df = pd.concat(polls, ignore_index=True)


#tranformation
combined_df = pd.merge(roster_df, polls_df, how='left', left_on='netid', right_on='student_id')
# merge() is a function that combines two dataframes based on a common column
st.dataframe(combined_df)

# poll count by each date
poll_counts = combined_df.pivot_table(index='date', values='poll_num', aggfunc='max')
st.dataframe(poll_counts)

# count of student responses by date
student_responses = combined_df.pivot_table(index='netid', columns='date', values='answer', aggfunc='count')
student_responses = student_responses.fillna(0)
st.dataframe(student_responses)

# change student poll response to percentanges
student_pct = student_responses.copy()
for col in student_pct.columns:
    student_pct[col] = student_responses[col] / poll_counts.loc[col, 'poll_num']
st.dataframe(student_pct)

# convert percentanges to grades
student_graded = student_pct.copy()
for col in student_graded.columns:
    student_graded[col] = student_graded[col].apply(grade)
st.dataframe(student_graded)


summary = student_responses.copy()
summary['sessions'] = len(summary.columns)
summary['AB'] = summary.apply( lambda row: row.value_counts().get('AB', 0), axis=1)
summary['np'] = summary.apply( lambda row: row.value_counts().get('AB', 0), axis=1)
summary['Pct'] = summary['AB']  + summary['np'] / summary['sessions'] 

summary_with_names = pd.merge(roster_df, summary, left_on = 'netid', right_index=True)
st.title("Xavier Polling Report")
st.dataframe(summary_with_names)
st.download_button("Download Report", summary_with_names.to_csv(), "poll-report.csv")
