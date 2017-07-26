# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:16:42 2017

@author: mpr
"""

import json


def parsejson(jsonfile):
    """
    This module parses the json returned by the url request
    and then returns the longitude, latitude, and the address 
    of the place.
    
    """
    latitude = json.dumps([s['geometry']['location']['lat'] for s in jsonfile['results']], indent=3)
    latitude = float(latitude.strip("[]"))
    longitude = json.dumps([s['geometry']['location']['lng'] for s in jsonfile['results']], indent=3)
    longitude = float(longitude.strip("[]"))
    return latitude
    return longitude
    
