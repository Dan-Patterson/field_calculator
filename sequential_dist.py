
# https://community.esri.com/t5/python-documents/distance-calculations-in-the-field-calculator/ta-p/916461
x0 = 0.0
y0 = 0.0
import math
def dist_between(shape):
    """Useage ... dist_between(!Shape!)"""
    global x0
    global y0
    x = shape.firstpoint.X
    y = shape.firstpoint.Y
    if x0 == 0.0 and y0 == 0.0:
        x0 = x
        y0 = y
    distance = math.sqrt((x - x0)**2 + (y - y0)**2)
    x0 = x
    y0 = y
    return distance
