import numpy as np
from numpy import pi, r_
import matplotlib.pyplot as plt
from scipy import optimize
import scipy.signal
from scipy.interpolate import UnivariateSpline, splrep, splev


proA = np.loadtxt("proA.txt")
proB = np.loadtxt("proB.txt")
proC = np.loadtxt("proC.txt")
proD = np.loadtxt("proD.txt")
aTx = proA[:,0]
atX = proA[:,1]
bTx = proB[:,0]
btX = proB[:,1]
dTx = proD[:,0]
dtX = proD[:,1]

peakind = scipy.signal.find_peaks_cwt(atX, np.arange(1,20))
print peakind
spl = UnivariateSpline(aTx, atX,k=5)
tck = splrep(aTx, atX, k=5,s=1000)
plt.plot(aTx, spl(aTx), 'g', lw=1)
peak_aTx = []
peak_atX = []
for i in peakind:
	peak_aTx.append(aTx[i])
	peak_atX.append(atX[i])
print aTx[peak_aTx[3]]-aTx[peak_aTx[2]]
a_period = 2
print a_period
def a_angles(t):
	real_t = t % a_period
	print real_t
	return splev(real_t+aTx[122],tck) 
xxx= np.arange(0,100,0.001)
np.savez("spline_A",tck)
plt.plot(xxx,a_angles(xxx))
plt.show()