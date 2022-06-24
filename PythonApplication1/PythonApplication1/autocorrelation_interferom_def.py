



# autocorrelation_interferom_def.py

import numpy as np
#import matplotlib.pyplot as plt
#import math



def proc1(param=0.01,m=128):




#tcol = np.zeros((m,1)); # Electric field


    tcol = np.zeros((m,1)); # difference

    #imcol = np.zeros((m,1)) #% 

    Etcol = np.zeros((m,1)); # Electric field

    freq = 1
    omega = 2*np.pi*freq
 
    #print('omega=')
    #print(omega)



    for ii in range(m):
        for jj in range(m):

        #d = ii * 0.025

        #print(item1)
     
            time1 = jj * 0.025
            tcol[(jj)] = time1

            Et = np.exp(1j * omega * time1) * (np.exp(-(time1))**2/1) + param * np.exp(1.j * omega * time1) * (np.exp(-(time1-3))**2/1)
            #Et = math.sin(omega * time1)

            Etcol[(jj)] = Et

    return tcol, Etcol


