import numpy as np
from numpy import pi, r_
import matplotlib.pyplot as plt
from scipy import optimize
import scipy.signal
from scipy.interpolate import UnivariateSpline

letra = raw_input()
proA = np.loadtxt("pro"+letra+".txt")

Tx = proA[:,0]
tX = proA[:,1]
tX = scipy.signal.medfilt(tX,kernel_size=11)
spl = UnivariateSpline(Tx, tX)
plt.plot(Tx, spl(Tx), 'g', lw=3)
plt.show()