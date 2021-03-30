import numpy as np
import math as m
  
def Rx(theta):
  return np.matrix([[ 1, 0           , 0           ],
                   [ 0, m.cos(theta),-m.sin(theta)],
                   [ 0, m.sin(theta), m.cos(theta)]])
  
def Ry(theta):
  return np.matrix([[ m.cos(theta), 0, m.sin(theta)],
                   [ 0           , 1, 0           ],
                   [-m.sin(theta), 0, m.cos(theta)]])
  
def Rz(theta):
  return np.matrix([[ m.cos(theta), -m.sin(theta), 0 ],
                   [ m.sin(theta), m.cos(theta) , 0 ],
                   [ 0           , 0            , 1 ]])

def function(X, phi, theta, psi, f, Xd):
    X = X-Xd
    X = np.dot(Rz(phi), X)
    X = np.dot(Ry(theta), X)
    X = np.dot(Rx(psi), X)
    u = f*X[1]/X[0]
    v = f*X[2]/X[0]
    return [u,v]
    
