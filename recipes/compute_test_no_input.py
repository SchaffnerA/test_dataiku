# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu



# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

test_no_input_df = ... # Compute a Pandas dataframe to write into test_no_input


# Write recipe outputs
test_no_input = dataiku.Dataset("test_no_input")
test_no_input.write_with_schema(test_no_input_df)
