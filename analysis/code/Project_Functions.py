
# This file is used for cleaning Temperature datasets

import pandas as pd

def DataClean(file):
    # Create a Dataframe from each file, and skips the first 31 rows

    Data_Clean = pd.read_csv(file, usecols=['Stn_Name', 'Prov', 'Tm', 'S', 'P'], skiprows=31)
    
    # Data cleaning for the Canadian Temperature datasets in the raw folder
    data_clean = pd.read_csv(file, usecols=['Stn_Name', 'Prov', 'P', 'S', 'Tm'], sep = ",", skiprows=31)
    
    # I am assuming a nan value for snowfall and precipitation implies that
    # there was no data collected for these values within given time period.
    # Therefore, replace these NaN values with 0.
    
    NanValues = {'S':0, 'P':0}
    data_clean.fillna(value = NanValues, inplace=True)
    
    # Insert columns for Year and Month, for useful data analysis, 
    # These values are extracted from the file name
    date = file[24:31].strip(".").split("_")
    data_clean.insert(0, 'Year', date[0], allow_duplicates = True) # date[0] gives the year
    data_clean.insert(1, 'Month', date[1], allow_duplicates = True) # date[1] gives the month
    
    # Consider all other rows with NaN values to be invalid data, drop all these rows.
    data_clean.dropna(inplace = True)

    # Reset index of 'cleaned' dataframe
    data_clean.reset_index(inplace=True, drop=True)
    
    return Data_Clean
