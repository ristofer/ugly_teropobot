import numpy as np
from numpy import pi, r_
import matplotlib.pyplot as plt
from scipy import optimize
import scipy.signal
from scipy.interpolate import UnivariateSpline, splev, splrep

filll = np.load("juanito.npz")
tck=filll["arr_0"]
print tck
def b_angles(t):
	real_t = t % 2
	print real_t
	return splev(real_t+4.081279275,tck) 
xxx= np.arange(0,30,0.00001)
plt.plot(xxx,b_angles(xxx))
plt.show()