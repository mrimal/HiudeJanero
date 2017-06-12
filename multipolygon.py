# -*- coding: utf-8 -*-
"""
Created on Thu May 4 15:14:18 2017

@author: mpr
"""
from __future__ import print_function
import csv
import re
import paths
from shapely.geometry import Polygon, Point, MultiPolygon
import shapefile
import pandas as pd

goodlist = []

path = paths.shapefilePath

polygon = shapefile.Reader(path)

polygon = polygon.shapes()

shpfilePoints = [shape.points for shape in polygon]

polygons = shpfilePoints


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
        
                
#findInsideOut(point)

#dataframe = pd.read_csv("outputfile.csv")
#Using CSV reader to read the geocordinates from the earlier files and checking
#to see if they fall inside or outside.

#They can both be run seperately but we will have to wait to run them together.
def loopsandFind():
    with open(paths.exportFile) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            address = row['1'].decode('iso-8859-1').encode('utf8')
            rowfirst = row['0']
            firstrow = re.split(',', rowfirst)
            latitude = float(firstrow[0].strip("("))
            longitude = float(firstrow[1].strip(")"))
            geocod = Point(longitude, latitude)
            print(geocod)
            print(address)
            findInsideOut(geocod, address)
            '''
def export_final():
    final_table = pd.DataFrame(goodlist, index=None)
    final_table.to_csv('goodpoints.csv', encoding="utf-8")
    
def main():
    loopsandFind()
    export_final()
    
if __name__ == '__main__':
    main()
    
    
