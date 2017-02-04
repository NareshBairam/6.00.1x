#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:45:06 2017

@author: naresh
"""
from math import pi, tan
def polysum(n, s):
    """
    n: number of sides of a regular polygon
    s: length of each side
    returns: the sum of the area and the square of the perimeter of the polygon, rounded to 4 decimal places
    """
    area = (0.25*n*s**2)/tan(pi/n)
    perimeter = (n*s)**2
    return round(area + perimeter, 4)
    