# -*- coding: utf-8 -*-
"""

@author: mpr
"""
import shapefile
import fiona
import pandas as pd
from pandas import DataFrame
import shapely
from shapely.geometry import shape,mapping, Point, Polygon, MultiPolygon

polygon = shapefile.Reader('./shp/33MUE250GC_SIR.shp') 
polygon = polygon.shapes()  
shpfilePoints = []
#print(polygon)
for randomthings in polygon:
    shpfilePoints = randomthings.points 
    #print(shape.points)
newShape = shapely.geometry.asShape(polygon['geometry'] )
print(newShape)
'''

df_points = pd.read_csv('HiuCSV.csv')
# point in polygon test
for point in df_points:
    if polygon.contains(point):
        print 'inside'
    else:
        print "OUT" 
''' 
