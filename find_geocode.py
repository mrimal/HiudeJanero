# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:07:00 2017

@author: mpr
"""
import paths
from geopy.geocoders import GoogleV3
import pandas as pd
import numpy as np

successList = []
failureList = []
geolocator = GoogleV3(api_key=paths.API)




def locate(x):
    print("'" + x + "'")
    location = geolocator.geocode(x)  # Get geocode
    print(location)
    lat = location.latitude
    lon = location.longitude
    try:
        #Get geocode
        location = geolocator.geocode(x, timeout=8, exactly_one=True)
        lat = location.latitude
        lon = location.longitude
    except AttributeError:
        print("Couldn't find it")
        lat = np.nan
        lon = np.nan
        pass
        #didn't work for some reason that I really don't care about
        #lat = np.nan
        #lon = np.nan
        #print(lat,lon)
    return pd.Series([lat,  lon])

"""
df_geo = pd.DataFrame(columns = ['BIG_ADDR', 'LAT', 'LON'])
df_geo['BIG_ADDR'] =  df = df_addr['street'] + ' ' +  df_addr['neighboorhood'] + ' ' + df_addr['STATE'] + ' ' +  \
                       df_addr['ZIP_CODE'] 
# Eliminate dups
df_geo = df_geo['BIG_ADDR'].drop_duplicates().reset_index()

# Geocode ALL THINGS in GEO frame!
df_geo[['LAT','LON']] = df_geo['BIG_ADDR'].apply(locate)

# Create the same index in the address dataframe
df_addr['BIG_ADDR'] =  df = df_addr['CITY'] + ' ' +  df_addr['PROVINCE'] + ' ' + df_addr['STATE'] + ' ' +  \
                       df_addr['ZIP_CODE'] + ' ' + df_addr['COUNTRY'] 

# Combine the address and geo frames 
df_addr = pd.merge(df_addr, df_geo, on=['BIG_ADDR'], how='left') 
df_addr.rename(columns={'LAT_y': 'LAT', 'LON_y': 'LON'}, inplace=True)           #cleanup
df_addr.rename(columns={'LAT_y': 'LAT', 'LON_y': 'LON'}, inplace=True)
del df_geo['index']
"""
