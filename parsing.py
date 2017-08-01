# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:16:42 2017

@author: mpr
"""

import findaddress
import fileexport

eList = []

address = findaddress.findaddress("3203 SE Woodstock Blvd., Portland, OR 97202")

eList.append(address)
    
address2 = findaddress.findaddress("79th SE 88th Avenue, Portland, OR 97216")
eList.append(address2)