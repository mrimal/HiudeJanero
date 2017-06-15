    # -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:46:08 2017
@author: mpr
"""
from __future__ import print_function
import glob
import csv
import paths
import multipolygon
import pandas as pd
from geopy.geocoders import GoogleV3

#defining the two types of list and google API.
successlist = []
failurelist = []
geolocator = GoogleV3(api_key=paths.API)


#Making an address class, so everything that an address goes through
#is here and is easy to handle.
class brokenAddress(object):
    """
    Including everything to do with an address in an address class
    so everything is in the same place and easily accessible cross
    module as well. This will be helpful when the project gets too
    big. While this is not complete yet, as there still needs to be things
    that need to be done to include the addresses that are broken.
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
        address2 = self.street + "," + self.neighbourhood + "," + self.state_name + self.zipcode
        print(address)
        location = geolocator.geocode(address, timeout=10)
        if location:
            success = [location, "First try"]
            successlist.append(success)
        else:
            failurelist.append(address)
            failurelocation = geolocator.geocode(address2, timeout = 10)
            if failurelocation:
                success2 = [failurelocation, "Second Try - without State"]
                successlist.append(success2)
                
                


def main(filepath):
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

                addressChunk = brokenAddress(street, neighbourhood, municipal, state_name, zipcode, country)
                addressChunk.findAddress()
                #print(addressChunk)

#Saving the files to excel
def csvExport():
    """
    This gives us the lists we have created with addresses that passed and
    failed as csvs. This can be improved by just defining csvexport(list) to give
    us csv for any file. This would be one place where the code would change in
    the final version.
    """
    final_table = pd.DataFrame(listname, index=None)
    file = filename + '.csv' 
    final_table.to_csv(file, encoding='utf-8')


if __name__ == '__main__':
    main(paths.testfile)
    csvExport(successlist, 'good')
    csvExport(failurelist, 'bad')
    multipolygon.main()
