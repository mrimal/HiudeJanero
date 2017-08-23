# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:07:00 2017

@author: mpr
"""
import paths
from geopy.geocoders import GoogleV3
import pandas as pd
import numpy as np

geolocator = GoogleV3(api_key=paths.API)

def locate(x):
    #print("'" + x + "'")
    #location = geolocator.geocode(x)  # Get geocode
    #print(location)
    #lat = location.latitude
    #lon = location.longitude
    try:
        #Get geocode
        location = geolocator.geocode(x, timeout=10)
        lat = location.latitude
        lon = location.longitude
        print(lat, lon)
    except:
        #didn't work for some reason that I really don't care about
        lat = np.nan
        lon = np.nan
        #print(lat,lon)
    return pd.Series([lat,  lon])
    print(pd.Series([lat, lon]))
def fileread(filepath):
    """
    Create a new dataframe that has the address, latitude, and longitude, 
    and then apply the locate function to the dataframe, and fill in the 
    lat/lon empty boxes with whatever the function returns.
    
    This should help us create one table with everything in it.
    """
    df_addr = pd.read_csv(filepath)[1:8]
    df_geo = pd.DataFrame(columns = ['BIG_ADDR', 'LAT', 'LON'])
    df_geo['BIG_ADDR'] = df = df_addr['street'] + "," + df_addr['neighboorhood'] + "," + \
                                df_addr['municipal'] + "," + df_addr['state_name']
    df_geo['BIG_ADDR'] = df_geo['BIG_ADDR'].drop_duplicates().reset_index()
    df_geo = df_geo.replace('\s+', ' ', regex=True)
    df_geo[['LAT','LON']] = (df_addr['street'] + "," + df_addr['neighboorhood'] + "," + df_addr['municipal'] + "," + df_addr['state_name']).apply(locate)
    #df_geo[['LAT','LON']] = locate(df_geo['BIG_ADDR'])
    df_geo.to_csv("filepath.csv")
    return df_geo
    print(df_geo)
fileread(paths.testfile)
