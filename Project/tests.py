from math import *
import sys

def cone(h,r):
    volume = (1/3 * pi * r*r* h)
    surface_area = (pi * r * (r + sqrt(h*h + r*r)))
    return [round(volume,2), round(surface_area,2)]

def cube(s):
    volume = (s*s*s)
    surface_area = (6* s*s)
    return [round(volume,2), round(surface_area,2)]

def cylinder(h,r):
    volume = (pi * r*r*  h)
    surface_area = (2 * pi * r * h + 2 * pi * r*r)
    return [round(volume,2), round(surface_area,2)]

def runtests(a,b,c,d,e):
    conevals = cone(float(a),float(b))
    cubevals = cube(float(c))
    cylindervals = cylinder(float(d),float(e))

    shapevols = [conevals[0], cubevals[0], cylindervals[0]]
    shapeareas = [conevals[1], cubevals[1], cylindervals[1]]

    return [max(shapeareas),max(shapevols)]


