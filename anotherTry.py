# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:03:48 2017

@author: mpr
"""

import fiona
import shapely
from shapely.geometry import Point
import paths
    
with fiona.open(paths.shapefilePath) as fiona_collection:
    
    # In this case, we'll assume the shapefile only has one record/layer (e.g., the shapefile
    # is just for the borders of a single country, etc.).
    shapefile_record = fiona_collection.next()
    #print(shapefile_record)
    # Use Shapely to create the polygon
    shape = shapely.geometry.asShape(shapefile_record['Geometry'])
    print(shape)
    #point = shapely.geometry.Point(-43.414, -22.392) # longitude, latitude
    point = Point(-43.0302544, -22.7920041) # longitude, latitude
    print(point)
        
        
    # Alternative: if point.within(shape)
    if shape.contains(point):
        print "Found shape for point."
    else:
        print "What up"
                
    if point.within(shape):
        print "Yo yo yo"
    else:
        print "what up myaan"
            
