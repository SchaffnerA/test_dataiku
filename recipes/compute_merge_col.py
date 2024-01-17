# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
fake_data = dataiku.Dataset("fake_data")
fake_data_df = fake_data.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.
fake_data_df['col_merged'] = fake_data_df['Name'] + fake_data_df['email']
merge_col_df = fake_data_df # For this sample code, simply copy input to output


# Write recipe outputs
merge_col = dataiku.Dataset("merge_col")
merge_col.write_with_schema(merge_col_df)
