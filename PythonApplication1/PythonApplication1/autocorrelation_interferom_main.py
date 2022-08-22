
#autocorrelation_interferom_main.py

import numpy as np
import matplotlib.pyplot as plt

import autocorrelation_interferom_def

param = 0.005
m = 256

tcol, Etcol, Signalcol = autocorrelation_interferom_def.proc1(param,m)


print('')
print('autocorrelation_interferom_main.py')
print('')


fig1 = plt.figure(figsize = (10,6), facecolor='lightblue')

ax1 = fig1.add_subplot(2, 2, 1) # Real
ax2 = fig1.add_subplot(2, 2, 2) # Imaginary
ax3 = fig1.add_subplot(2, 2, 3) # Power
ax4 = fig1.add_subplot(2, 2, 4)

ax1.plot(tcol,np.real(Etcol))

ax2.plot(tcol,np.imag(Etcol))

ax3.plot(tcol,np.angle(Etcol))

ax4.plot(tcol,np.real(Signalcol))


#fig2 = plt.figure(figsize = (10,6), facecolor='lightblue')
#bx1 = fig2.plot(tcol,np.real(Signalcol))
#bx1.xlabel("Delay")



plt.show()

    


