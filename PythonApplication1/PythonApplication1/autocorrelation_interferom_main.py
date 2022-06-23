
#autocorrelation_interferom_main.py

import numpy as np

import autocorrelation_interferom_def

aaa = autocorrelation_interferom_def.proc1(1)

import matplotlib.pyplot as plt



print('Start Main')


m = 128
tcol = np.zeros((m,1))   # time
dcol = np.zeros((m,1)) # difference
imcol = np.zeros((m,1)) #% 
Etcol = np.zeros((m,1)); # Electric field


freq = 1
omega = 2*np.pi*freq
 
print('omega=')
print(omega)



for ii in range(m):
  for jj in range(m):

    #d = ii * 0.025

     #print(item1)
     
    time1 = jj * 0.025
    tcol[(jj)] = time1

    Et = np.exp(1j * omega * time1) * (np.exp(-(time1))**2/1) + aaa * np.exp(1.j * omega * time1) * (np.exp(-(time1-3))**2/1)
    Etcol[(jj)] = Et

     #td = d
     #Etd = 1

     



print(tcol)
print(Etcol)

plt.plot(tcol,Etcol)

#      print("list1=", item1, ", list2=", item2)
    



