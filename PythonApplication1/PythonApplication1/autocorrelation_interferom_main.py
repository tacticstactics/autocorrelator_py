
#autocorrelation_interferom_main.py

import numpy as np
import matplotlib.pyplot as plt

import autocorrelation_interferom_def

freq = 8
# Frequency of Carrier wave

pulsewidth = 0.8
# Pulsewidth

m = 256
# Number of Sampling

steptime = 0.025
#step time


tcol, Etcol, Signalcol = autocorrelation_interferom_def.proc1(freq,pulsewidth,m,steptime)


print('')
print('autocorrelation_interferom_main.py')
print('')


fig1 = plt.figure(figsize = (10,6), facecolor='lightblue')

ax1 = fig1.add_subplot(2, 2, 1) # Real part of Interference
ax2 = fig1.add_subplot(2, 2, 2) # Imaginary part of Interference
ax3 = fig1.add_subplot(2, 2, 3) # Phase
ax4 = fig1.add_subplot(2, 2, 4) # Power of Interferogram 

ax1.plot(tcol,np.real(Etcol))
ax2.plot(tcol,np.imag(Etcol))
ax3.plot(tcol,np.angle(Etcol))
ax4.plot(tcol,np.real(Signalcol))

ax1.set_ylabel("Real Part of electric field")
ax2.set_ylabel("Imaginary Part of electric field")

ax3.set_xlabel("Delay")
ax4.set_xlabel("Delay")

ax3.set_ylabel("Phase")

ax4.set_ylabel("Second Harmonic Generation Signal")

#fig2 = plt.figure(figsize = (10,6), facecolor='lightblue')
#bx1 = fig2.plot(tcol,np.real(Signalcol))
#bx1.xlabel("Delay")

plt.show()  

#End of File
