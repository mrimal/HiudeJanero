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

geolocator = GoogleV3(api_key=paths.API)

def saveTabletoExcel(listName, fileName):
    final_table = pd.DataFrame(listName, index=None)
    x = fileName + '.xlsx'
    writer = pd.ExcelWriter(x)
    final_table.to_excel(writer, 'Sheet1')
    writer.save()
#gmaps = googlemaps.Client(key=paths.API)

#Defining Geocodes function which returns the address in coordinate format
def findGeocodes(addressChunk, successList, failureList):
    successList = []
    failureList = []
    for address in addressChunk:
        print(address)
        location = geolocator.geocode(address, timeout = 10)
        if location:
            successList.append(location)
        else:
            failureList.append(address)
    


for each in glob.iglob(paths.fileLocNew):
    # Geocoding an address
    #print(each)
    
    df_mc = pd.read_csv(each)[1:10]
    
    #dfShortened = df_mc.ix[:,1:250]
    
    #print(dfShortened)
    
    #streetnames = df_mc['street'] 
    streetNeigh = df_mc['street'] + "," +  df_mc['neighboorhood'] + ",Sao Goncalo, Rio de Janeiro," 
    #print(streetNeigh)   
    
    findGeocodes(streetNeigh, geocode1, geocodeError1)

#Saving the files to excel 
saveTabletoExcel(geocode1, 'OutputFile')
saveTabletoExcel(geocodeError1, 'ErrorFile')