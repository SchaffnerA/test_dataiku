# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
place = dataiku.Dataset("place")
place_df = place.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

place_with_new_col_df = place_df # For this sample code, simply copy input to output


# Write recipe outputs
place_with_new_col = dataiku.Dataset("place_with_new_col")
place_with_new_col.write_with_schema(place_with_new_col_df)
