import numpy as np
from numpy import pi, r_
import matplotlib.pyplot as plt
from scipy import optimize
import scipy.signal
from scipy.interpolate import UnivariateSpline, splev, splrep


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
btX = scipy.signal.medfilt(btX,kernel_size=3)
peakind = scipy.signal.find_peaks_cwt(btX, np.arange(1,20))
print peakind
spl = UnivariateSpline(bTx, btX,k=5)
tck = splrep(bTx, btX, k=5,s=2000)
plt.plot(bTx, spl(bTx), 'g', lw=1)
peak_bTx = []
peak_btX = []
for i in peakind:
	peak_bTx.append(bTx[i])
	peak_btX.append(btX[i])
print bTx[peak_bTx[3]]-bTx[peak_bTx[2]]
b_period = 2
print b_period
def b_angles(t):
	real_t = t % b_period
	print real_t
	return splev(real_t+bTx[122],tck) 
xxx= np.arange(0,30,0.00001)
print aTx
print bTx
print "tupla"
print tck
np.savez("spline_B",tck)
print "12222"
print bTx[122]
plt.plot(xxx,b_angles(xxx))
plt.show()