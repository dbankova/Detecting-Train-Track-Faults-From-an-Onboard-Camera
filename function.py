import numpy as np

# Transformation matrix from real 3D space to 2D image space
def transformation_matrix(f, angles, coordinates, campos):
    theta,phi,psi = angles
    # Rotation matrices
    R1 = np.matrix([[ 1, 0           , 0           ],
                   [ 0, np.cos(psi), np.sin(psi)],
                   [ 0, -np.sin(psi), np.cos(psi)]])
    R2 = np.matrix([[ np.cos(theta), 0, -np.sin(theta)],
                   [ 0           , 1, 0           ],
                   [ np.sin(theta), 0, np.cos(theta)]])
    R3 = np.matrix([[ np.cos(phi), np.sin(phi), 0 ],
                   [ -np.sin(phi), np.cos(phi) , 0 ],
                   [ 0           , 0            , 1 ]])
    new_coords = np.dot(np.dot(R1,np.dot(R2,R3)),coordinates-campos)
    return f*np.array([new_coords[0,1],new_coords[0,2]])/new_coords[0,0]

g = 1.435 # track gauge
w = 0.11 # track width
h = 2.165 # camera height
f = 0.0058 # focal length

# Camera position in 3D space
campos = np.array([0,0.6,0])

# theta (the pitch angle), phi (yaw angle) and psi (the roll angle)
angles = np.array([-0.3333578871,-0.1270599695,0])

xmax = 40 # max value of x we look ahead to in metres
N = 50 # mesh
x=np.linspace(0,xmax,N) # range from 0 to xmax metres, split up with the mesh number N

ylo = (g/2+w)*np.ones(N) # left outer
yli = g/2*np.ones(N) # left inner
yro = (-g/2-w)*np.ones(N) # right outer
yri = -g/2*np.ones(N) # right inner

z = -h*np.ones(50) # we take camera to be the origin, so track is at -h

Xlo = np.array([x,ylo,z])
Xlo = np.array([x,ylo,z])
Xlo = np.array([x,ylo,z])
Xlo = np.array([x,ylo,z])


coordinates = np.array([1,2,3])
u,v = transformation_matrix(f, angles, coordinates, campos)
print(u,v)
