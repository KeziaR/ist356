import streamlit as st


## Challenge 2-2-1

# Write a streamlit to input a length and width of a rectangle,
#  and output the permieter 2 x (L+W) and area (L x W) of that rectangle 

# use a "calculate" button and a "clear" button 

# use `st.number_input()` for numbers


def rectangle_setup():
    if PERIMETER:
        peri
    elif AREA:
       area

def clear_click():
    len = None
    wid = None

st.title("Calculating Length and Width of a Rectangle")

len = st.number_input("Input length of rectangle")
wid = st.number_input("Input width of rectangle")
peri = 2 * (len + wid) 
area =  len * wid
PERIMETER = st.button("Calculate Perimeter", on_click = rectangle_setup)
AREA = st.button("Calculate AREA", on_click = rectangle_setup)
st.button("Clear", on_click = clear_click)




