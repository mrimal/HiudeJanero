# -*- coding: utf-8 -*-
"""
@author: mpr
"""

from shapely.geometry import Polygon, Point, MultiPolygon
import shapefile

polygon = shapefile.Reader('test/shp/33MUE250GC_SIR.shp') 
polygon = polygon.shapes()  
shpfilePoints = [shape.points for shape in polygon]

#print(shpfilePoints)

polygons = shpfilePoints
for polygon in polygons:
    poly = Polygon(polygon)
    #print(poly)
    
point = Point(-43.0479848, -22.8091922)        
if polygons.contains(point):
    print 'inside'
else:
    print 'OUT'
'''
for shape in polygon:
    shpfilePoints = shape.points 
poly = shpfilePoints 
poly = Polygon(poly)


point = Point(-22.8091922, -43.03798848)
# point in polygon test
if poly.contains(point):
    print 'inside'
else:
    print 'OUT'
'''
