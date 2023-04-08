
# This file is used for cleaning Temperature datasets

import pandas as pd

def DataClean(file):
    # Create a Dataframe from each file, and skips the first 31 rows
    Data_Clean = pd.read_csv(file, usecols=['Stn_Name', 'Prov', 'P', 'S', 'Tm'], sep = ",", skiprows=31)
    
    # Insert columns for Year and Month, for useful data analysis, 
    # These values are extracted from the file name
    date = file[24:31].strip(".").split("_")
    Data_Clean.insert(0, 'Year', date[0], allow_duplicates = True) # date[0] gives the year
    Data_Clean.insert(1, 'Month', date[1], allow_duplicates = True) # date[1] gives the month
    
    # Consider all other rows with NaN values to be invalid data, drop all these rows.
    Data_Clean.dropna(inplace = True)

    # Reset index of 'cleaned' dataframe
    Data_Clean.reset_index(inplace=True, drop=True)
    
    return Data_Clean
