
# This file is used for cleaning Temperature datasets

import pandas as pd

def DataClean(file):
    # Create a Dataframe from each file, and skips the first 31 rows

    Data_Clean = pd.read_csv(file, usecols=['Stn_Name', 'Prov', 'Tm', 'S', 'P'], skiprows=31)
    
    # I am considering a 0 in Snowfall or Precipation columns to mean
    # that there was no data was available to collect for the time period
    Data_Clean.replace({'S':0, 'P':0}, inplace=True)
    
    # Exract Year and Month from file name
    date = file[30:37].strip(".").split("_")
    
    Data_Clean.insert(0, 'Year', int(date[0])) # date[0] gives the year
    Data_Clean.insert(1, 'Month', int(date[1])) # date[1] gives the month
    
    # Drop all other NaN values from our dataframes
    Data_Clean.dropna(inplace=True)
    
    # Resets index as many changes were made to create dataframes
    Data_Clean.reset_index(inplace=True, drop=True)
    
    return Data_Clean
