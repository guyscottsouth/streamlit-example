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
        abs(np.random.randn(7, 10)*1000),
        columns=('col %d' % i for i in range(7)))


df = get_dataframe()
df = df.round(2)
df.columns = ['Mon','Tues','Wed','Thur','Fri','Sat','Sun']

st.table(df.style.format('£{0:,.2f}'))
