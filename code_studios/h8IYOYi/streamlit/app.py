import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import dataiku

st.title('Hello Streamlit!')

filtered = dataiku.Dataset("filtered")
filtered_df = filtered.get_dataframe()
st.write("First five lines of the DataFrame:")
st.write(filtered_df.head())