# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:46:08 2017
@author: mpr
"""

import paths
from geopy.geocoders import GoogleV3, Nominatim, Bing

successList = []
failureList = []
geoloc_goog = GoogleV3(api_key=paths.API)
geoloc_osm = Nominatim()
#geoloc_bing = Bing()

def goog(addressChunk):
    for address in addressChunk:
        print(address)
        location = geoloc_goog.geocode(address, timeout = 10)
        if location:
            successList.append(location)
        else:
            failureList.append(address)
    

def osm(addressChunk):
    for address in addressChunk:
        print(address)
        location = geoloc_osm.geocode(address)
        if location:
            print(location)
            successList.append(location)
        else:
            failureList.append(address)
"""
def bing(addressChunk):
    for address in addressChunk:
        print(address)
        location = geoloc_bing.geocode(address)
        if location:
            successList.append(location)
        else:
            failureList.append(address)
"""
