# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:46:08 2017
@author: mpr
"""
from __future__ import print_function
import glob
#import pandas as pd
import csv
import paths
from geopy.geocoders import GoogleV3

#Class exercise.
successList = []
failureList = []
geolocator = GoogleV3(api_key=paths.API)


#Making an address class, so everything that an address goes through
#is here and is easy to handle.
class brokenAddress(object):
    """
    Including everything to do with an address in an address class
    so everything is in the same place and easily accessible cross
    module as well. This will be helpful when the project gets too
    big
    """
    def __init__(self, street, neighbourhood, municipal, state_name, zipcode, country):
        self.street = street
        self.neighbourhood = neighbourhood
        self.municipal = municipal
        self.state_name = state_name
        self.zipcode = zipcode
        self.country = country
    #Finding address at first with the four main points
    def findAddress(self):
        """Finding address for the largest address group"""
        address = self.street + "," + self.neighbourhood + "," + self.municipal +"," + self.state_name
        print(address)
        location = geolocator.geocode(address, timeout=10)
        if location:
            successList.append(location)
        else:
            failureList.append(address)



for each in glob.iglob(paths.testfile):
    with open(each) as csvfile:
        reader = csv.DictReader(csvfile)
        for df_mc1 in reader:
            street = df_mc1['street']
            neighbourhood = df_mc1['neighboorhood']
            municipal = df_mc1['municipal'].decode('iso-8859-1').encode('utf8')
            state_name = df_mc1['state_name']
            zipcode = df_mc1['zipcode']
            country = df_mc1['country']

            jamesy = brokenAddress(street, neighbourhood, municipal, state_name, zipcode, country)
            jamesy.findAddress()
            print(jamesy.street)
            print(jamesy.municipal)
