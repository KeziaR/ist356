import streamlit as st
import pandas as pd

def clean_currency(value):
    cleaning = value.replace('$', '').replace(',','')

def detect_whale(
        items_per_person:float, 
        price_per_person:float, 
        items_per_person_75th_pctile:float, 
        price_per_person_75_pctile:float) -> str:
    if items_per_person > items_per_person_75th_pctile and price_per_person > price_per_person_75_pctile:
        return 'whale'
    if items_per_person > items_per_person_75th_pctile:
        return 'big eater'
    if price_per_person > price_per_person_75_pctile:
        return 'big spender'
    
    return ''

def detect_tipper(tip_pct, tip_pcy_75th_pctile, tip_pct_25_pctile):
    if 

    return 0


if __name__=='__main__':

    assert clean_currency('$1,000.00') == 1000.00
    assert clean_currency('$1,000') == 1000.00
    assert clean_currency('1,000') == 1000.00
    assert clean_currency('$1000') == 1000.00

    ppp_75 = checks['price_per_person'].quantile(0.75)
    ipp_75 = checks['items_per_person'].quantile(0.75)
    print(ppp_75, ipp_75)
    assert detect_whale(5, 250, 3, 175) == 'whale'
    assert detect_whale(5, 100, 3, 175) == 'big eater'
    assert detect_whale(1, 250, 3, 175) == 'big spender'
    assert detect_whale(1, 100, 3, 175) == ''

    assert detect_tipper(tip_percentage = 0.20, tip_pct_25_pctile= 0.25, 0.15) == 1

