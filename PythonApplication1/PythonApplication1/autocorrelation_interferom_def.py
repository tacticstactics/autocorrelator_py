


# autocorrelation_interferom_def.py

import numpy as np
#import matplotlib.pyplot as plt
#import math


def proc1(param=0.01,m=128):



#tcol = np.zeros((m,1)); # Electric field

    tcol = np.zeros((m,1)); # time
    delaycol = np.zeros((m,1)); # difference

    imcol = np.zeros((m,1)); #% 

    Etcol = np.zeros((m,1)); # Electric field

    freq = 1
    omega = 2*np.pi*freq
 
    print('omega=')
    print(omega)



    for ii in range(m):

        delay = ii * 0.025-6
        a = 0
        aa = 0

        for jj in range(m):



        #print(item1)
     
            time1 = jj * 0.025
            tcol[(jj)] = time1

            Et = np.exp(1j * omega * time1) * (np.exp(-(time1))**2/1) + param * np.exp(1.j * omega * time1) * np.exp(-(time1-3))**2/(1**2)
            #Et = math.sin(omega * time1)

            Etcol[(jj)] = Et

            td = time1 + delay

            Etd = np.exp(1j * omega * time1) * (np.exp(-(time1))**2/1) + param * np.exp(1.j * omega * time1) * np.exp(-(time1-3))**2/(1**2)

            aa = a+np.abs((Et + Etd)**2)**2
            a = aa

            imcol[(ii)] = aa
            delaycol[(ii)] = delay


    return tcol, Etcol


