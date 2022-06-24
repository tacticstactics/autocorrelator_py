
#autocorrelation_interferom_main.py

import numpy as np
import matplotlib.pyplot as plt
import math

import autocorrelation_interferom_def

param = 0.01
m = 128

tcol, Etcol = autocorrelation_interferom_def.proc1(param,m)


print('')
print('autocorrelation_interferom_main.py')
print('')

plt.plot(tcol,np.real(Etcol))
#plt.plot(tcol,np.imag(Etcol))

plt.show()

#      print("list1=", item1, ", list2=", item2)
    


