
#autocorrelation_interferom_main.py

import numpy as np
import matplotlib.pyplot as plt
import math

import autocorrelation_interferom_def

param = 0.01
m = 128

tcol, Etcol, delaycol, Etdmtrx, imcol = autocorrelation_interferom_def.proc1(param,m)


print('')
print('autocorrelation_interferom_main.py')
print('')
print("Etdmtrx Shape", Etdmtrx.shape)


fig = plt.figure(figsize = (10,6), facecolor='lightblue')

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)

ax1.plot(tcol,np.real(Etcol))
ax2.plot(delaycol,imcol)

plt.show()

#fig2 = plt.figure(figsize = (10,6), facecolor='lightblue')
#ax3 = fig2.add_subplot(2, 2, 1)
#ax4 = fig2.add_subplot(2, 2, 2)

#plt.show()

#      print("list1=", item1, ", list2=", item2)
    


