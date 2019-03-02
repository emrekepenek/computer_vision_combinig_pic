
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as mat
import numpy as np
import pymesh

fig = mat.figure()
ax = fig.add_subplot(111, projection= 'rectilinear')

def read_off(file):
    if 'OFF' != file.readline().strip():
        raise('Not a valid OFF header')
    n_verts, n_faces, n_dontknow = tuple([int(s) for s in file.readline().strip().split(' ')])
    verts = [[float(s) for s in file.readline().strip().split(' ')] for i_vert in range(n_verts)]
    faces = [[int(s) for s in file.readline().strip().split(' ')][1:] for i_face in range(n_faces)]
    return verts, faces

def column(matrix, i):
    return [row[i] for row in matrix]

mesh = open("armadillo.off")
print("yunus")
vects , facess= read_off(mesh)
print(vects)

angel = np.array([[ 0.9948391, -0.0821202, 0.0595940 ],[ 0.0912277, 0.9810261, -0.1710711], [ -0.0444148, 0.1756248, 0.9834548 ]])

vects=np.array(vects)

for x in vects:
    x=np.matmul(x,angel)

print(vects[0])
f=5
count=0

for x in vects:
    a=x[2].__abs__()
    x[0]=(x[0]/a)*f
    x[1] = (x[1] / a) * f
    x[2]=f
    if(x[0]>100000):
        print(x)
    if (x[0] < -100000):
        print(x)

    count=count+1
ax.scatter(column(vects,0),column(vects,1),column(vects,2),c='r',marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')

print(vects[0])
ax.set_ylim([-20000,20000])
ax.set_xlim([-20000,20000])
mat.show()