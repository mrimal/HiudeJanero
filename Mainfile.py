# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:46:08 2017

@author: mpr
"""

#Things to Do:
    #Geoocde the addresses using a couple of different APIs.
        #Save addresses that were not geocoded. 
    #Data validation check using the provided shape files.
    #Data validation can be done at a municipal level rather than state level.
        #List of errors saved as 'address',[lat,long] pairs. 

#import googlemaps
from geopy.geocoders import GoogleV3
#from datetime import datetime
import paths
import glob
import pandas as pd
from pandas import DataFrame

geocode = []

geolocator = GoogleV3(api_key=paths.API)

#gmaps = googlemaps.Client(key=paths.API)

for each in glob.iglob(paths.filename):
    # Geocoding an address
    
    municipal_code = each
    df_mc = pd.read_csv(municipal_code,sep=',',encoding = 'latin1')
    streetnames = df_mc['addr']
    for streets in streetnames:
        location = geolocator.geocode(streets, timeout = 10)
   # print((location.latitude, location.longitude))
        if location:
            geocode.append(location)
            print((location.latitude, location.longitude)) 
     # Look up an address with reverse geocoding
    #reverse_geocode_result = gmaps.reverse_geocode((, ))
    
    # Request directions via public transit
final_table = pd.DataFrame(geocode, index=None)
writer = pd.ExcelWriter('ShortOutput.xlsx')
final_table.to_excel(writer, 'Sheet1' )
writer.save()
