# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:22:39 2017

@author: mpr
"""
import urllib
import json
import paths

def findaddress(address):
    """
    This function returns the longitude and latitude
    of the json result that the google API returns
    so that it is easy to write to a file.
    
    A speedtest returned that this was a tad bit slower
    than using the GEOLOC and GMAPS commands.
    """
    URL2 = "https://maps.googleapis.com/maps/api/geocode/json?address="
    URL = URL2 + str(address)
    URL = URL + "&key=" + paths.API
    print(URL)
    googleResponse = urllib.urlopen(URL)
    print(googleResponse)
    json_location = json.loads(googleResponse.read())
    latitude = json.dumps([s['geometry']['location']['lat'] for s in json_location['results']], indent=3)
    latitude = float(latitude.strip("[]"))
    longitude = json.dumps([s['geometry']['location']['lng'] for s in json_location['results']], indent=3)
    longitude = float(longitude.strip("[]"))
    return latitude
    return longitude
    
