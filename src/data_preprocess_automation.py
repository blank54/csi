import os
import pandas as pd

def import_data(fpath):
    return pd.read_excel(fpath)

def preprocess(fpath):
    data_raw = import_data(fpath)

    # TODO: write code to automate the data preprocessing.



    return preprocessed_data