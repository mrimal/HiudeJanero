# -*- coding: utf-8 -*-
"""
Created on Thu May 4 15:14:18 2017

@author: mpr
"""
from __future__ import print_function
import csv
import re
import paths
import fileexport
from shapely.geometry import Polygon, Point, MultiPolygon
import shapefile
import pandas as pd

path = paths.shapefilePath

polygon = shapefile.Reader(path)

polygon = polygon.shapes()

shpfilePoints = [shape.points for shape in polygon]

polygons = shpfilePoints

goodlist = []
#defining the function that sees if the files are available inside the point
# or not.
def findInsideOut(point, address):
    for polygon in polygons:
        poly = Polygon(polygon)
        #print poly
        if poly.contains(point):
            print('inside')
            x = [point, address, "inside"]
            goodlist.append(x)
        
def loopsandFind():
    """
    Using CSV reader to read the geocordinates from the earlier files and checking
    to see if they fall inside or outside.
    """
    with open(paths.exportFile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            latitude = float(row['0'])
            longitude = float(row['1'])
            address = row['2']
            geocod = Point(longitude, latitude)
            findInsideOut(geocod, address)
    
def main():
    loopsandFind()
    fileexport.csv_export(goodlist, "foundaddy")
    
if __name__ == '__main__':
    main()
    
    
