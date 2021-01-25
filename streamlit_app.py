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
        round(abs(np.random.randn(5, 5)*1000),2),
        columns=('col %d' % i for i in range(5)))


df = get_dataframe()
df.columns = ['Mon','Tues','Wed','Thur','Fri']

st.table(df.style.highlight_max(axis=0))
