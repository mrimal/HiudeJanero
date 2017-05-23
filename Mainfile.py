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
        
from geopy.geocoders import GoogleV3
import paths
import glob
import pandas as pd
import multipolygon 

successList = []
failureList = []
geolocator = GoogleV3(api_key=paths.API)

#Defining findGeocodes function which returns the address in coordinate format
def findGeocodes(addressChunk):
    for address in addressChunk:
        print(address)
        location = geolocator.geocode(address, timeout = 10)
        if location:
            successList.append(location)
        else:
            failureList.append(address)
    return successList
    return failureList

def readingFiles():   
    for each in glob.iglob(paths.fileLocNew):
        # Geocoding an address
        df_mc = pd.read_csv(each)[1:12]    
        #streetnames = df_mc['street'] 
        streetNeigh = df_mc['street'] + "," +  df_mc['neighboorhood'] + ",Sao Goncalo, Rio de Janeiro," 
        #print(streetNeigh)   
        findGeocodes(streetNeigh)

#readingFiles(paths.fileLocNew)    
#Saving the files to excel 
def csvExport():
    final_table = pd.DataFrame(successList, index=None)
    final_table.to_csv('good.csv', encoding='utf-8')
    final_table = pd.DataFrame(failureList, index=None)
    final_table.to_csv('bad.csv', encoding='utf-8')
    
def main():
    readingFiles()
    csvExport()
    multipolygon.main()


if __name__ == '__main__':
    main()
