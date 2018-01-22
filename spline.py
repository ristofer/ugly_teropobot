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

for i,angle in enumerate(dtX):
	if angle<0:
		dtX[i] = 180
dtX = scipy.signal.medfilt(dtX,kernel_size=11)

peakind = scipy.signal.find_peaks_cwt(dtX, np.arange(1,20))
print peakind
spl = UnivariateSpline(dTx, dtX,k=5)
tck = splrep(dTx, dtX, k=5,s=1000)
plt.plot(dTx, spl(dTx), 'g', lw=1)
peak_dTx = []
peak_dtX = []
for i in peakind:
	peak_dTx.append(dTx[i])
	peak_dtX.append(dtX[i])
d_period = 2
print d_period
def d_angles(t):
	real_t = t % d_period
	print real_t
	return splev(real_t+dTx[122],tck) 
xxx= np.arange(0,10,0.001)
np.savez("spline_D",tck)
plt.plot(xxx,d_angles(xxx))
plt.show()