from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

"""
# Welcome to Guy's Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

def get_dataframe():
    return pd.DataFrame(
        np.random.randn(5, 5),
        columns=('col %d' % i for i in range(5)))


df = get_dataframe()
df.columns = ['Mon','Tues','Wed','Thur','Fri']

st.table(df.style.highlight_max(axis=0))
