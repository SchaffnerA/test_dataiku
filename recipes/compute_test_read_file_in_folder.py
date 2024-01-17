# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
test_folder = dataiku.Folder("kihEvHXM").get_path()

path_of_csv = os.path.join(folder_path, "geoplaces2 - geoplaces2.csv") 
my_dataset = pd.read_csv(path_of_csv)


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

test_read_file_in_folder_df = ... # Compute a Pandas dataframe to write into test_read_file_in_folder


# Write recipe outputs
test_read_file_in_folder = dataiku.Dataset("test_read_file_in_folder")
test_read_file_in_folder.write_with_schema(test_read_file_in_folder_df)
