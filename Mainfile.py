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

import paths
import findgeocodes
import glob
import pandas as pd
import fileexport
#import multipolygon 

newlist = []

def readingFiles():
    """
    This reades the files from all the 
    directories in the path.
    This is a test line added. 
    """  
    for each in glob.iglob(paths.splitfile):
        # Geocoding an address
        df_mc = pd.read_csv(each)[2800:5000]  
        #streetnames = df_mc['street'] 
        streetNeigh = df_mc['street'] + "," +  df_mc['neighboorhood'] + ",Sao Goncalo, Rio de Janeiro" 
        streetNeigh = streetNeigh.drop_duplicates()
        streetNeigh = streetNeigh.replace('\s+', ' ', regex=True)
        #print(streetNeigh)   
        #try:
        findgeocodes.findgeocodes(streetNeigh)
        
#readingFiles(paths.fileLocNew)    
#Saving the files to excel 
    
def main():
    readingFiles()
    fileexport.csv_export(findgeocodes.successList, 'good')
    fileexport.csv_export(findgeocodes.failureList, 'bad')
    fileexport.csv_export(newlist, 'messedup')    
    #multipolygon.main()


if __name__ == '__main__':
    main()
