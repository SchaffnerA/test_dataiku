# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
place = dataiku.Dataset("place")
place_df = place.get_dataframe()




place_with_new_col_df = place_df # For this sample code, simply copy input to output
place_with_new_col_df['new_col'] = place_with_new_col_df['latitude']+place_with_new_col_df['longitude']


# Write recipe outputs
place_with_new_col = dataiku.Dataset("place_with_new_col")
place_with_new_col.write_with_schema(place_with_new_col_df)
