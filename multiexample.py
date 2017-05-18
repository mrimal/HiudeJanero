# -*- coding: utf-8 -*-
"""
Created on Thu May 18 15:14:18 2017

@author: mpr
"""

from shapely.geometry import Polygon, Point, MultiPolygon

import shapefile
import paths

path = paths.shapefilePath

polygon = shapefile.Reader(path)

polygon = polygon.shapes()

shpfilePoints = [shape.points for shape in polygon]

#print shpfilePoints

polygons = shpfilePoints

point = Point(-43.08885660000001, -22.8603561)        

for polygon in polygons:
    poly = Polygon(polygon)
    #print poly
    if poly.contains(point):
        print 'inside'

