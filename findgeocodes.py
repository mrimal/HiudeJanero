# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:46:08 2017
@author: mpr
"""
from __future__ import print_function
import googlemaps
from datetime import datetime
import glob
import csv
import paths
import json
import fileexport
import urllib
#import multipolygon
from geopy.geocoders import GoogleV3

success_list = []
failure_list = []
GEOLOC = GoogleV3(api_key=paths.API)
GMAPS = googlemaps.Client(key=paths.API)


def find_address(address):
    """
    This function returns the longitude and latitude
    of the json result that the google API returns
    so that it is easy to write to a file.
    
    A speedtest returned that this was a tad bit slower
    than using the GEOLOC and GMAPS commands.
    
    """
    URL2 = "http://maps.googleapis.com/maps/api/geocode/json?address="
    URL = URL2 + str(address)
    googleResponse = urllib.urlopen(URL)
    print(googleResponse)
    json_location = json.loads(googleResponse.read())
    latitude = json.dumps([s['geometry']['location']['lat'] for s in json_location['results']], indent=3)
    longitude = json.dumps([s['geometry']['location']['lng'] for s in json_location['results']], indent=3)
    print(latitude)
    print(longitude)

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
                #country = df_mc1['country']

                address = street + "," + neighbourhood + "," + municipal + "," \
                            + state_name
                f_address = street + "," + neighbourhood + "," + zipcode + "," \
                            + state_name

                #location = GEOLOC.geocode(address, timeout=10)
                find_address(address)
                if location:
                    slist = (latitude, longitude, address, "First try")
                    #slist = (location.latitude, location.longitude, location.address, address, "First try")
                    success_list.append(slist)
                    print("found")
                else:
                    failure_list.append(address)
                    location2 = GMAPS.geocode(f_address)
                    #location2 = GEOLOC.geocode(f_address, timeout=10)
                    if location2:
                        slist = (latitude, longitude, f_address, "Second try without key")
                        #slist = (location, address, "First try")
                        #slist = (location2.latitude, location2.longitude, location2.address, f_address, "Second try")
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
