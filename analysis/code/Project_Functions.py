
# This file is used to combine all Temperature data

import pandas as pd

def DataCombine(list):
    # Gets a list of datasets, to combine all into one for easier analysis
    
    for i in list:
        df1 = DataClean(list[0])
        df2 = DataClean(i)
        Data_Combine = pd.concat([df1, df2], keys=['Year', 'Month', 'Stn_Name', 'Prov'], join="outer", ignore_index=True)
    
    return Data_Combine

def DataClean(file):
    # Create a Dataframe from each file, and skip the first 31 rows of the temperature datasets

    Data_Clean = pd.read_csv(file, usecols=['Stn_Name', 'Prov', 'S', 'P', 'Tm'], skiprows=31)
    
    # I am considering a 0 in Snowfall or Precipation columns to mean
    # that there was no data was available to collect for the time period
    Data_Clean.replace({'S':0, 'P':0}, inplace=True)
    
    # Exract Year and Month from file name
    date = file[30:37].strip(".").split("_")
    
    Data_Clean.insert(0, 'Year', date[0], allow_duplicates=False) # date[0] returns the year
    Data_Clean.insert(1, 'Month', date[1], allow_duplicates=False) # date[1] returns the month
    
    # pd.to_numeric will help to ensure dtype is what we want them to be
    Data_Clean["Year"] = pd.to_numeric(Data_Clean["Year"], errors='coerce', downcast='signed')
    Data_Clean["Month"] = pd.to_numeric(Data_Clean["Month"], errors='coerce', downcast='signed')
    Data_Clean["S"] = pd.to_numeric(Data_Clean["S"], errors='coerce', downcast='signed')
    Data_Clean["P"] = pd.to_numeric(Data_Clean["P"], errors='coerce', downcast='signed')
    Data_Clean["Tm"] = pd.to_numeric(Data_Clean["Tm"], errors='coerce', downcast='signed')
    
    # Drop all other NaN values from our dataframes
    Data_Clean.dropna(inplace=True)
    
    # Resets index as many changes were made to create dataframes
    Data_Clean.reset_index(inplace=True, drop=True)
    
    return Data_Clean