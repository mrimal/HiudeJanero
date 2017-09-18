# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:46:08 2017
@author: mpr
"""
#from __future__ import print_function
#from datetime import datetime
import glob
#import csv
#import re
import paths
import pandas as pd
import fileexport
import findaddress
#import findgeocodes
#from geopy.geocoders import GoogleV3
#import multipolygon

success_list = []
failure_list = []
#GEOLOC = GoogleV3(api_key=paths.API)
#GMAPS = googlemaps.Client(key=paths.API)

def findcodes(filepath):
    """
    This finds the files from the txt file
    and then creates address chunks which
    can be sent to find geocodes
    This will check to see if an address
    can be returned by google maps API
    or not. This will return the good address
    in a list called success_list and addresses
    which cannot be found in another list
    failure_list.
    """
    for each in glob.iglob(filepath):
        """
        https://stackoverflow.com/questions/1546226/
            a-simple-way-to-remove-multiple-spaces-in-a-string-in-python/
            15913564#15913564
        Speed test for different methods used to strip a string of whitespaces
        """
        #with open(each) as csvfile:
            #reader = csv.DictReader(csvfile)
        df_mc = pd.read_csv(each)[1:12]
        #for df_mc1 in df_mc:
        for index, row in df_mc.iterrows():
            street = row['street']
            neighbourhood = row['neighboorhood']
            municipal = row['municipal']
            #municipal.decode('iso-8859-1').encode('utf8')
            state_name = row['state_name']
            zipcode = row['zipcode']
            #country = df_mc1['country']
            address = str(street) + "," + str(neighbourhood) + "," + \
                          str(municipal) + "," + str(zipcode) + "," \
                              + str(state_name)
            address = address.decode('iso-8859-1').encode('utf8')
            while '  ' in address:
                address = address.replace('  ', ' ')
            f_address = str(street) + "," + str(neighbourhood) + "," +  \
                        str(zipcode) + "," \
                        + str(state_name)
            while '  ' in f_address:
                f_address = f_address.replace('  ', ' ')
            #address_df = pd.DataFrame(address, index=None)
            location = findaddress.findaddress(address)
            if location:
                slist = location['address'], location['long'], location['lat'], address, "First Try"
                success_list.append(slist)
                print("found")
            else:
                failure_list.append(address)
                location2 = findaddress.findaddress(f_address)
                if location2:
                    slist = [location2, f_address, "Second try"]
                    success_list.append(slist)
           

def main():
    """
    Run all the functions created in the
    file. These include finding the geocodes,
    exporting them to files, and then finding
    whether or not they fall within the specified
    shapefile.
    """
    findcodes(paths.testfile)
    fileexport.csv_export(success_list, "good")
    fileexport.csv_export(failure_list, "bad")
    #multipolygon.main()

if __name__ == '__main__':
    main()
