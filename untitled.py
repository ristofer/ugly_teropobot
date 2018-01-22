#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from mpl_toolkits.mplot3d import Axes3D
from numpy import ma
#mpl.rcParams['xtick.labelsize'] = 30 
#mpl.rcParams['ytick.labelsize'] = 30 
proA = np.loadtxt("proA.txt")
#ax.scatter(odom[:,1],odom[:,2],odom[:,3])
#ax.scatter(aruco[:,1],aruco[:,2],aruco[:,3])
#plt.xlim(-3,3)
#plt.ylim(-3,3)
#ax.set_zlim(-3,3)
#ax.zlim(-3,3)

plt.figure(1)
plt.subplot(411)
plt.plot(aruco[:,0],aruco_x)
plt.plot(odom[:,0],odom[:,1])
plt.plot(orb[:,0],orb[:,1])
plt.subplot(412)
plt.plot(aruco[:,0],aruco_y)
plt.plot(odom[:,0],odom[:,2])
plt.plot(orb[:,0],orb[:,2])
plt.subplot(413)
plt.plot(aruco[:,0],aruco_z)
plt.plot(odom[:,0],odom[:,3])
plt.plot(orb[:,0],orb[:,3])
plt.show()
# X = np.array([1798.00 ,1798.00, 1798.00, 1678.00, 1619.00, 1439.00 ,1200.00, 842.00 ,478, 0])
# Y = np.array([0 ,1.114119052, 3.36425467, 5.189596843 ,10.94456643, 16.81234777, 19.25313117 ,18.70515744 ,14.31024456, 0])
# Z = np.array([0.00 ,1.80 ,1.65, 1.65,2.12, 2.12 ,1.73, 1.61 ,3.37 ,0.00])
# plt.figure()
# plt.xlabel('Velocidad [rpm]',fontsize=40)
# plt.ylabel('Eficiencia [%]',fontsize=40)
# plt.errorbar(X, Y, yerr=Z, fmt='o')
# plt.title('Eficiencia calculada con su error para velocidad de bomba de 60%', fontsize=48)


# plt.show()

