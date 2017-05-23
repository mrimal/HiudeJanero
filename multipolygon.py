# -*- coding: utf-8 -*-
"""
Created on Thu May 4 15:14:18 2017

@author: mpr
"""

from shapely.geometry import Polygon, Point, MultiPolygon

import shapefile
import paths
#import pandas as pd
import csv 
import re

path = paths.shapefilePath

polygon = shapefile.Reader(path)

polygon = polygon.shapes()

shpfilePoints = [shape.points for shape in polygon]

#print shpfilePoints

polygons = shpfilePoints

#point = Point(-43.0048131, -22.8232439)        

#defining the function that sees if the files are available inside the point
# or not.
def findInsideOut(point):
    for polygon in polygons:
        poly = Polygon(polygon)
        #print poly
        if poly.contains(point):
            print 'inside'

#findInsideOut(point)

#dataframe = pd.read_csv("outputfile.csv")
#Using CSV reader to read the geocordinates from the earlier files and checking
#to see if they fall inside or outside.

#They can both be run seperately but we will have to wait to run them together. 

with open(paths.exportFile) as csvfile:
    reader=csv.DictReader(csvfile)
    
    for row in reader:
        x = row['1']
        #print(x)
        y = re.split(',', x)
        #print(y)
        latitude = float(y[0].strip("("))
        longitude = float(y[1].strip(")"))
        x = Point(longitude, latitude)
        print(x)
        findInsideOut(x)
