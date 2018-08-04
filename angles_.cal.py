# -*- coding: utf-8 -*-
import numpy as np

def angles_poly(a, inside=True, in_deg=True):
    """Sequential angles from a poly* shape
	NOTE: this line.... angle = np.sum(angles)
	      can be changed to `np.min`, `np.max` or others
		  depending on what needs to be returned
    """
    a = a.getPart()
    a =np.asarray([[i.X, i.Y] for j in a for i in j])
    if len(a) < 2:
        return None
    elif len(a) == 2:  # **** check
        ba = a[1] - a[0]
        return np.arctan2(*ba[::-1])
    else:
        angles = []
        if np.allclose(a[0], a[-1]):  # closed loop
            a = a[:-1]
            r = (-1,) + tuple(range(len(a))) + (0,)
        else:
            r = tuple(range(len(a)))
        for i in range(len(r)-2):
            p0, p1, p2 = a[r[i]], a[r[i+1]], a[r[i+2]]
            ba = p1 - p0
            bc = p1 - p2
            cr = np.cross(ba, bc)
            dt = np.dot(ba, bc)
            ang = np.arctan2(np.linalg.norm(cr), dt)
            angles.append(ang)
    if in_deg:
        angles = np.degrees(angles)
    angle = np.sum(angles)
    return angle
#__esri_field_calculator_splitter__
#angles_poly(!Shape!)