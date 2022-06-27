


# autocorrelation_interferom_def.py

import numpy as np
#import matplotlib.pyplot as plt
import math


def proc1(param=0.01,m=128):



#tcol = np.zeros((m,1)); # Electric field

    tcol = np.zeros((m,1)); # time
    delaycol = np.zeros((m,1)); # difference
    
    Etcol = np.ones(m, dtype=complex)*2
    imcol = np.zeros((m,1)); #% 

    freq = 100
    omega = 2*np.pi*freq
 
    print('omega=')
    print(omega)

    tau = 0.1


    for ii in range(m):

        delay = ii * 0.025-6
        a = 0
        aa = 0

        for jj in range(m):



        #print(item1)
     
            time1 = 0.025 * jj -1.6
            tcol[(jj)] = time1

            #Et = math.sin(omega * time1)
            #Et = np.exp(1j * omega * time1)
            
            Et = np.exp(1j * omega * time1) * np.exp(-1.38 * (time1/tau)**2)
            
            
            #print("Complex")
            #print(Et)
            #print("Real")
            #print(Et.real)
            #print("Imag")
            #print(Et.imag)
            
            #print(type(Et.real))
            #print(type(Et.imag))

            Etcol[(jj)] = Et

            td = time1 + delay

            #Etd = np.exp(1j * omega * time1) * (np.exp(-(time1))**2/1) + param * np.exp(1.j * omega * time1) * np.exp((-(time1-3))**2/(1**2))
            Etd = math.sin(omega * time1) * math.sin(omega * td)

            aa = a+np.abs((Et + Etd)**2)**2
            a = aa

            imcol[(ii)] = aa
            delaycol[(ii)] = delay


    return tcol, Etcol, delaycol, imcol


