# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:46:08 2017

@author: mpr
"""

#Things to Do:
    #Geoocde the addresses using a couple of different APIs.
        #Save addresses that were not geocoded. 
    #Data validation check using the provided shape files.
    #Data validation can be done at a municipal level rather than state level.
        #List of errors saved as 'address',[lat,long] pairs. 

import googlemaps
from datetime import datetime
import paths


gmaps = googlemaps.Client(key=paths.API)


# Geocoding an address
geocode_result = gmaps.geocode('1818 H St NW')

print(geocode_result)
# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((, ))

# Request directions via public transit
now = datetime.now()
