import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import dataiku
import shap
st.title('Table')

new_df = dataiku.Dataset("merge_col")
new_df = new_df.get_dataframe()
st.write("First five lines of the DataFrame:")
st.write(new_df.head())
