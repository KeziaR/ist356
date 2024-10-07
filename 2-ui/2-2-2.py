import streamlit as st 


#initialize 
if 'total' not in st.session_state:
    st.session_state.count = 0.0
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("Order total and history")

enter = st.number_input("Enter item, press add to total for total, or press clear to exit")


add_total = st.button("add to total")
clear = st.button("clear")


while True: 
    if enter == 0:
        break
    elif add_total == True:
        st.session_state.count += 1
        st.session_state.history.append(enter)
        st.write(f"Total order is {st.session_state.count}")
    else:
        st.session_state.history == True
        st.session_state.count = None