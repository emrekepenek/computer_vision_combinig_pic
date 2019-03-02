
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as mat
import numpy as np

fig = mat.figure()
ax = fig.add_subplot(111, projection=None)

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
print(vects.__len__())


vects=np.array(vects)

for x in vects:
    x[0]=x[0]-1.5
    x[2]=x[2]-0.75

print(vects)
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
create = open("armadillo2.off",'w+')
create.writelines('OFF \n')
create.writelines(str(vects.__len__())+' '+str(facess.__len__())+' 0 \n')
for x in vects:
    a=x[0]
    b=x[1]
    c=x[2]
    create.writelines(str(a)+' '+str(b)+' '+str(c)+'\n')
for x in facess:
    print(x)
    a=x[0]
    b=x[1]
    c=x[2]
    create.writelines(str(3)+' '+str(a)+' '+str(b)+' '+str(c)+'\n')
create.close()
ax.scatter(column(vects,0),column(vects,1),column(vects,2),c='r',marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_ylim([-20000,20000])
ax.set_xlim([-20000,20000])
print(vects[0])
mat.show()