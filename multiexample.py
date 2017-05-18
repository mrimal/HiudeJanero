# -*- coding: utf-8 -*-
"""
Created on Thu May 18 15:14:18 2017

@author: mpr
"""

from shapely.geometry import Polygon, Point, MultiPolygon

import shapefile
import paths
#import pandas as pd
#from pandas import DataFrame
import csv 

path = paths.shapefilePath

polygon = shapefile.Reader(path)

polygon = polygon.shapes()

shpfilePoints = [shape.points for shape in polygon]

#print shpfilePoints

polygons = shpfilePoints

point = Point(-43.0048131, -22.8232439)        

def findInsideOut(point):
    for polygon in polygons:
        poly = Polygon(polygon)
        #print poly
        if poly.contains(point):
            print 'inside'

#findInsideOut(point)

#dataframe = pd.read_csv("outputfile.csv")

with open('outputfile.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    
    for row in reader:
        print(row['lat '], row['long '])
        x = Point(float(row['long ']), float(row['lat ']))
        print(x)
        findInsideOut(x)