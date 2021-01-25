from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

"""
# Trading Report

"""

def get_dataframe():
    return pd.DataFrame(
        abs(np.random.randn(5, 7)*1000),
        columns=('col %d' % i for i in range(7)))


df = get_dataframe()
df = df.round(2)
df.columns = ['Mon','Tues','Wed','Thur','Fri','Sat','Sun']
df.index = ['143 - York 1', '206 - York 2','493 - York Monks Cross','395 - Hull 2','960 - Hull 3']

st.table(df.style.format('£{0:,.2f}'))
