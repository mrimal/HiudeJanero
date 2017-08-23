# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:07:00 2017

@author: mpr
"""
import paths
from geopy.geocoders import GoogleV3
import pandas as pd
from pandas import DataFrame
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

def fileread(filepath):
    df_addr = pd.read_csv(filepath)
    df_geo = pd.DataFrame(columns = ['BIG_ADDR', 'LAT', 'LON'])
    df_geo['BIG_ADDR'] = df = df_addr['street'] + "," + df_addr['neighboorhood'] + "," + \
                                df_addr['municipal'] + "," + df_addr['state_name']
    return df_geo