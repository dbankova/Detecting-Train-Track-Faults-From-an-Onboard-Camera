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
xmax = 40 #max value of x we look ahead to
x=np.array([0,xmax]) #range from 0 to xmax metres
y1 = np.array(g/2,-g/2) #INNER track for two values y= g/2 and -g/2
y2 = np.array(g/2+w,-g/2-w) #OUTER track for two values 
