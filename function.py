import numpy as np

# Transformation matrix from real 3D space to 2D image space
def transformation_matrix(angles):
    theta,phi,psi = angles
    # Potation matrices
    R1 = np.matrix([[ 1, 0           , 0           ],
                   [ 0, np.cos(psi), np.sin(psi)],
                   [ 0, -np.sin(psi), np.cos(psi)]])
    R2 = np.matrix([[ np.cos(theta), 0, -np.sin(theta)],
                   [ 0           , 1, 0           ],
                   [ np.sin(theta), 0, np.cos(theta)]])
    R3 = np.matrix([[ np.cos(phi), np.sin(phi), 0 ],
                   [ -np.sin(phi), np.cos(phi) , 0 ],
                   [ 0           , 0            , 1 ]])
    return np.dot(R1,np.dot(R2,R3))
#
#def function(X, phi, theta, psi, f, Xd):
#    X = X-Xd
#    X = np.dot(Rz(phi), X)
#    X = np.dot(Ry(theta), X)
#    X = np.dot(Rx(psi), X)
#    u = f*X[1]/X[0]
#    v = f*X[2]/X[0]
#    return [u,v]
#    

<<<<<<< Updated upstream
def function(X, phi, theta, psi, f, Xd):
    X = X-Xd
    X = np.dot(Rz(phi), X)
    X = np.dot(Ry(theta), X)
    X = np.dot(Rx(psi), X)
    u = f*X[1]/X[0]
    v = f*X[2]/X[0]
    return [u,v]

g = 1.435 #track gauge
w = 0.11 #track width
h = 2.165 #camera height

xd = 0 #x position of camera
yd = 0.6 #y position of camera
zd = 0 #z position of camera

theta = -0.3333578871 #pitch angle
phi = -0.1270599695 #yaw angle
psi = 0 #roll angle (this will change with horizontal train vibrations)

xmax = 40 #max value of x we look ahead to in metres
N = 50 #mesh
x=np.linspace(0,xmax,N) #range from 0 to xmax metres, split up with the mesh number N

ylo = (g/2+w)*np.ones(N) #left outer
yli = g/2*np.ones(N) #left inner
yro = (-g/2-w)*np.ones(N) #right outer
yri = -g/2*np.ones(N) #right inner

z = -h*np.ones(50) #we take camera to be the origin, so track is at -h

Xlo = np.array([x,ylo,z])
Xlo = np.array([x,ylo,z])
Xlo = np.array([x,ylo,z])
Xlo = np.array([x,ylo,z])
=======
angles = np.array([1,2,3])
print(transformation_matrix(angles))
>>>>>>> Stashed changes
