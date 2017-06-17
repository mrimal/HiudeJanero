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
import multipolygon 


def readingFiles():
    """
    This reades the files from all the 
    directories in the path.
    """"   
    for each in glob.iglob(paths.fileLocNew):
        # Geocoding an address
        df_mc = pd.read_csv(each)[1:12]    
        #streetnames = df_mc['street'] 
        streetNeigh = df_mc['street'] + "," +  df_mc['neighboorhood'] + ",Sao Goncalo, Rio de Janeiro," 
        #print(streetNeigh)   
        findgeocodes.findgeocodes(streetNeigh)

#readingFiles(paths.fileLocNew)    
#Saving the files to excel 
def csvExport():
    final_table = pd.DataFrame(findgeocodes.successList, index=None)
    final_table.to_csv('good.csv', encoding='utf-8')
    final_table = pd.DataFrame(findgeocodes.failureList, index=None)
    final_table.to_csv('bad.csv', encoding='utf-8')
    
def main():
    readingFiles()
    csvExport()
    multipolygon.main()


if __name__ == '__main__':
    main()
