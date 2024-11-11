
import streamlit as st

# ## Challenge 2-2-2

# ### Order total and history

# Write a streamlit to input an amount.

# create an "add to total" button to 
# accumulate the amount in the total

# create a "clear" button to reset the session vars

# display the total and the history of each item entered 

# HINT: you'll need to manage a list for history!



# initializing the session state so that when the count 
# is not in session_state it will be created
if 'count' not in st.session_state:
    st.session_state.count = 0 
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("Order Total and History")
st.write("Enter the amount of each item bought")
amount = st.number_input("Amount")
add_on = st.button('add to total', type = 'primary' )
clear = st.button('clear', type = 'secondary')


if clear:
    st.session_state.count = 0
    st.session_state.history = []
elif add_on:
    st.session_state.count = st.session_state.count + 1
    st.session_state.history.append(amount)
    st.write(f'Amount total: {st.session_state.count}')
    for i in st.session_state.history:
        st.write(i)




