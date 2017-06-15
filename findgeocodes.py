# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:46:08 2017
@author: mpr
"""
from __future__ import print_function
import paths
from geopy.geocoders import GoogleV3

success_list = []
failure_list = []
GEOLOC = GoogleV3(api_key=paths.API)


def goog(addresschunk):
    """
    This will check to see if an address
    can be returned by google maps API
    or not. This will return the good address
    in a list called success_list and addresses
    which cannot be found in another list
    failure_list.
    """
    for address in addresschunk:
        print(address)
        location = GEOLOC.geocode(address, timeout=10)
        if location:
            slist = [location.longitude, location.latitude, location.address, "First try"]
            success_list.append(slist)
        else:
            failure_list.append(address)

