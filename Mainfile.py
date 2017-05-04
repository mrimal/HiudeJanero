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
geocodeError = [] 
geocode1 = []
geocodeError1 = []
geolocator = GoogleV3(api_key=paths.API)

def saveTabletoExcel(listName, fileName):
    final_table = pd.DataFrame(listName, index=None)
    x = fileName + '.xlsx'
    writer = pd.ExcelWriter(x)
    final_table.to_excel(writer, 'Sheet1')
    writer.save()
#gmaps = googlemaps.Client(key=paths.API)

for each in glob.iglob(paths.fileLocNew):
    # Geocoding an address
    #print(each)
    
    df_mc = pd.read_csv(each)[1:25]
    
    #dfShortened = df_mc.ix[:,1:250]
    
    #print(dfShortened)
    
    #streetnames = df_mc['street'] 
    streetNeigh = df_mc['street'] + "," +  df_mc['neighboorhood'] + ",Sao Goncalo, Rio de Janeiro," 
    print(streetNeigh)   
   
    '''
    
    for streets in streetnames:
        location = geolocator.geocode(streets, timeout = 10)
    #print((location.latitude, location.longitude))
        if location:
            geocode.append(location)
            print((location.latitude, location.longitude)) 
        else:
            geocodeError.append(streets)
     # Look up an address with reverse geocoding
    #reverse_geocode_result = gmaps.reverse_geocode((, ))
    ''' 
    for total in streetNeigh:
        print(total)
        location = geolocator.geocode(total, timeout = 10)
        if location:
            geocode1.append(location)
            #print((location.latitude, location.longitude)) 
            print(location.address)
            print(total)
        else:
            geocodeError1.append(total)

#Saving the files to excel 
saveTabletoExcel(geocode1, 'OutputFile')
saveTabletoExcel(geocodeError1, 'ErrorFile')