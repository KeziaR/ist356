
import pandas as pd
import streamlit as st

# if 'x' not in st.session_state:
#     st.session_state.x = 0
# if st.button("click me"):
#     st.session_state.x = st.session_state.x + 10
# st.write(st.session_state.x)


data= [
{
"course" : { "code" : "ist256", "credits": "3" },
"enrolled" : [{ "name": "allie", "grade": 3.667 },{ "name": "bart", "grade": 2.667 }]
},
{
"course" : { "code" : "ist356", "credits": "3" },
"enrolled" : [{ "name" : "cory", "grade" : 3.00 }]
}
]

df = pd.json_normalize(data)

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Chris", "Dee", "Eddie", "Fiona"],
    "state": ["NY", "PA", "NY", "NY", "NJ", "NJ"],
    "age": [25, 30, 35, 40, 45, 50]
})

data = [
    {
        "course": {"code": "ist256", "credits": "3"},
        "enrolled": [{"name": "allie", "grade": 3.667},{"name": "bart", "grade": 2.667}]
        },
    {
        "course": {"code": "ist356", "credits": "3"},
        "enrolled": []
    }
]