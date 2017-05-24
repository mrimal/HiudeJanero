# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:46:08 2017
@author: mpr
"""

import paths
from geopy.geocoders import GoogleV3

successList = []
failureList = []
geolocator = GoogleV3(api_key=paths.API)

def findgeocodes(addressChunk):
    for address in addressChunk:
        print(address)
        location = geolocator.geocode(address, timeout = 10)
        if location:
            successList.append(location)
        else:
            failureList.append(address)
    return successList
    return failureList
