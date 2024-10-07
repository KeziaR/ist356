import streamlit as st




# Initialize session state
if "Len" not in st.session_state:
    st.session_state.Len = 0
if "Wid" not in st.session_state:
    st.session_state.Wid = 0

st.title("Perimeter and Area of a Rectangle")
Len = st.number_input("Enter the length of the rectangle")
Wid = st.number_input("Enter the width of the rectangle")
peri_form = 2 * (Len + Wid)
area_form = Len * Wid

perimeter = st.write(f"Perimeter of the rectangle is", {peri_form})
area = st.write(f"Area of the rectangle is", {area_form})
calc = st.button("Calculate")
clear = st.button("Clear")

if calc:
    if perimeter:
        st.success(perimeter)
    elif area:
        st.success(area)
    else:
        st.error("Please enter the length and width of the rectangle")
if clear:
    st.session_State.perimeter = None
    st.session_State.area = None
    st.rerun()