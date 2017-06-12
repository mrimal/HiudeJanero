# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:06:27 2017

@author: mpr
"""

from __future__ import print_function
import paths
#import os
import csv
#import findgeocodes
from geopy.geocoders import Nominatim, Bing

geocode_osm = Nominatim()
#geocode_bing = Bing()

with open(paths.testfile) as csvfile:
        reader = csv.DictReader(csvfile)
        for df_mc1 in reader:
            street = df_mc1['street']
            neighbourhood = df_mc1['neighboorhood']
            #municipal = df_mc1['municipal'].decode('iso-8859-1').encode('utf-8')
            municipal = "Sao Goncalo" 
            state_name = df_mc1['state_name']
            zipcode = df_mc1['zipcode']
            country = df_mc1['country']
            address = street + "," + neighbourhood + "," + municipal + "," + state_name + "," + zipcode + "," + country
            location = geocode_osm.geocode(address)
            #print(address)
            if location:
                print(" ")
            else:
                print(address)
                print(" ")

            #print(addressChunk)