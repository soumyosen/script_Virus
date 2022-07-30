import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lipid = pd.read_csv('lipid_pts.csv', names=['Residue', 'X', 'Y'])
lipid_x = lipid['X'].tolist()
lipid_y = lipid['Y'].tolist()
residue = lipid['Residue'].tolist()
#print(residue)

boundary = pd.read_csv('boundary3d.csv', sep=" ", names=['X', 'Y', 'Z'])
boundary_x = boundary['X'].tolist()
boundary_y = boundary['Y'].tolist()

x = (1, 0)
y = (0, 1)
pinf = float("inf")
ninf = float("-inf")


def twodpoints(a, b):
    pts = []
    for i, j in zip(a, b):
        pts.append((i,j))

    return pts

lipid_pts = twodpoints(lipid_x, lipid_y)
boundary_pts = twodpoints(boundary_x, boundary_y)
#print(boundary_pts)

def onsegment(boundpt1, pt, boundpt2):
    if (np.dot(pt, x) <= max(np.dot(boundpt1, x), np.dot(boundpt2, x)) and 
        np.dot(pt, x) >= min(np.dot(boundpt1, x), np.dot(boundpt2, x)) and
        np.dot(pt, y) <= max(np.dot(boundpt1, y), np.dot(boundpt2, y)) and
	np.dot(pt, y) >= min(np.dot(boundpt1, y), np.dot(boundpt2, y))):
         return True
    else:
         return False



def orientation(boundpt1, pt, boundpt2):
    value = ((np.dot(pt, y)-np.dot(boundpt1, y))*(np.dot(boundpt2, x)-np.dot(pt, x))) - ((np.dot(pt, x)-np.dot(boundpt1, x))*(np.dot(boundpt2, y)-np.dot(pt, y)))
    if value == 0:
        return 0
    elif value > 0:
	return 1
    else:
	return 2



def doIntersect(boundpt1, boundpt2, pt1, pt2):
    o1 = orientation(boundpt1, boundpt2, pt1)
    o2 = orientation(boundpt1, boundpt2, pt2)
    o3 = orientation(pt1, pt2, boundpt1)
    o4 = orientation(pt1, pt2, boundpt2)
    
    if (o1 != o2 and o3 != o4):
	return True
    elif (o1 == 0 and onsegment(boundpt1, pt1, boundpt2)):
	return True
    elif (o2 == 0 and onsegment(boundpt1, pt2, boundpt2)):
	return True
    elif (o3 == 0 and onsegment(pt1, boundpt1, pt2)):
	return True
    elif (o4 == 0 and onsegment(pt1, boundpt2, pt2)):
        return True
    else:
	return False



def isInside(boundaryptlist, pt):
    n = len(boundaryptlist)
    if (n < 3):
	return False

    count = 0    
    infinitept = (99999, np.dot(pt, y))
    for i in range(n-1):
        nextpt = i+1
        if doIntersect(boundaryptlist[i], boundaryptlist[nextpt], pt, infinitept):
            if orientation(boundaryptlist[i], pt, boundaryptlist[nextpt]) == 0:
                return onsegment(boundaryptlist[i], pt, boundaryptlist[nextpt])
            else:
                count = count+1

    if (count % 2) == 1:
        return True


#polygon = [(0, 0), (10, 0), (0, 10), (10, 10)]
#p = (3, 3)
#print(isInside(polygon, p))

#print(orientation((0, 0), (0, 5), (0, 10)))

lipidlist = []

for i, j in zip(lipid_pts, residue):
    if isInside(boundary_pts, i):
        lipidlist.append(j)


for k in range(len(lipidlist)):
    print(lipidlist[k]),

