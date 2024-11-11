import streamlit as st

# Challenge 2-2-3

# Order File processing

# Write a streamlit to input a text file with one line per order. 
# Samples are provided in the `data` folder, but each line should 
# have the amount of the order.

# output the number of orders and the total amount of all orders.

title = st.title('Order File Procesing')
txt_file = st.file_uploader = ('Upload a txt file', types = ['txt'])

order = txt_file 

for each_line in txt_file:
    with open(txt_file , 'r') as file:
        data = file.read().replace('n', '')
