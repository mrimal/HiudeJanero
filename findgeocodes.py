# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:46:08 2017
@author: mpr
"""
from __future__ import print_function
import paths
import glob
import csv
import fileexport

import pandas as pd
from pandas import DataFrame
from geopy.geocoders import GoogleV3

success_list = []
failure_list = []
GEOLOC = GoogleV3(api_key=paths.API)

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
        with open(each) as csvfile:
            reader = csv.DictReader(csvfile)
            for df_mc1 in reader:
                street = df_mc1['street']
                neighbourhood = df_mc1['neighboorhood']
                municipal = df_mc1['municipal'].decode('iso-8859-1').encode('utf8')
                state_name = df_mc1['state_name']
                zipcode = df_mc1['zipcode']
                country = df_mc1['country']

                address = street + "," + neighbourhood + "," + municipal + "," \
                            + state_name
                f_address = street + "," + neighbourhood + "," + zipcode + "," \
                            + state_name

                location = GEOLOC.geocode(address, timeout=10)
                if location:
                    slist = (location.latitude, location.longitude, location.address, address, "First try")
                    success_list.append(slist)
                else:
                    failure_list.append(address)
                    location2 = GEOLOC.geocode(f_address, timeout=10)
                    if location2:
                        slist = (location2.latitude, location2.longitude, location2.address, f_address, "Second try")
                        success_list.append(slist)
def main():
    findcodes(paths.testfile)
    fileexport.csv_export(success_list, "good")
    fileexport.csv_export(failure_list, "bad")

if __name__ == '__main__':
    main()