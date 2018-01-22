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
cTx = proC[:,0]
ctX = proC[:,1]
dTx = proD[:,0]
dtX = proD[:,1]
ctX = scipy.signal.medfilt(ctX,kernel_size=5)
peakind = scipy.signal.find_peaks_cwt(ctX, np.arange(1,20))
print peakind
spl = UnivariateSpline(cTx, ctX,k=5)
tck = splrep(cTx, ctX, k=5,s=1000)
plt.plot(cTx, spl(cTx), 'g', lw=1)
peak_cTx = []
peak_ctX = []
for i in peakind:
	peak_cTx.append(cTx[i])
	peak_ctX.append(ctX[i])
print cTx[peak_cTx[3]]-cTx[peak_cTx[2]]
c_period = 2
print c_period
def c_angles(t):
	real_t = t % c_period
	print real_t
	return splev(real_t+cTx[122],tck) 
xxx= np.arange(0,30,0.001)
print aTx
print cTx
np.savez("spline_C",tck)
plt.plot(xxx,c_angles(xxx))
plt.show()