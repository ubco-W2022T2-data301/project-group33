# Functions for data cleaning are in this file

import pandas as pd
import numpy as np

def DataClean(file):
    # Read in the csv file
    data_clean = pd.read_csv(file, skiprows=31)
    
    # Drop some unusable columns
    data_clean.drop(columns=['Lat','Long','S_G','BS','DwBS','BS%','Clim_ID'], inplace=True)
    
    return data_clean

def DropNanValues(file, columns):
    # Drop rows with Nan values from a given set of columns
    drop = file.dropna(columns, inplace = True)
    return drop

