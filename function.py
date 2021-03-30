import numpy as np
  
def Rx(theta):
  return np.matrix([[ 1, 0           , 0           ],
                   [ 0, np.cos(theta),-np.sin(theta)],
                   [ 0, np.sin(theta), np.cos(theta)]])
  
def Ry(theta):
  return np.matrix([[ np.cos(theta), 0, np.sin(theta)],
                   [ 0           , 1, 0           ],
                   [-np.sin(theta), 0, np.cos(theta)]])
  
def Rz(theta):
  return np.matrix([[ np.cos(theta), -np.sin(theta), 0 ],
                   [ np.sin(theta), np.cos(theta) , 0 ],
                   [ 0           , 0            , 1 ]])

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
x=np.linspace(0,xmax) #range from 0 to xmax metres

ylo = g/2+w #left outer
yli = g/2 #left inner
yro = -g/2-w #right outer
yri = -g/2 #right inner

z = -h #we take camera to be the origin, so track is at -h

Xlo = np.array([x,ylo,z])
Xlo = np.array([x,ylo,z])
Xlo = np.array([x,ylo,z])
Xlo = np.array([x,ylo,z])
