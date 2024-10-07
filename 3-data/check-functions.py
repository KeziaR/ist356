import streamlit as st
import pandas as pd

def clean_currency(value):
    cleaning = value.replace('$', '').replace(',','')


if __name__=='__main__':

    assert clean_currency('$1,000.00') == 1000.00
    assert clean_currency('$1,000') == 1000.00
    assert clean_currency('1,000') == 1000.00
    assert clean_currency('$1000') == 1000.00
