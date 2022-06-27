


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
    
    Etdmtrx = np.zeros((m,m)); #% 

    freq = 100
    omega = 2*np.pi*freq
 
    print('omega=')
    print(omega)

    tau = 0.1


    for ii in range(m):

        time1 = 0.025*ii-1.6
        a = 0
        aa = 0

            

        for jj in range(m):

            tcol[(ii)] = time1
            Et = np.exp(1j * omega * time1) * np.exp(-1.38 * (time1/tau)**2)

            #Et = math.sin(omega * time1)
            #Et = np.exp(1j * omega * time1)         
            
            
            #print("Complex")
            #print(Et)
            #print("Real")
            #print(Et.real)
            #print("Imag")
            #print(Et.imag)
            
            #print(type(Et.real))
            #print(type(Et.imag))

            Etcol[(ii)] = Et

     
            delay1 = 0.025 * jj -0.08
            delaycol[(jj)] = delay1
        

            td = time1 + delay1

            #Etd = np.exp(1j * omega * time1) * (np.exp(-(time1))**2/1) + param * np.exp(1.j * omega * time1) * np.exp((-(time1-3))**2/(1**2))
            Etd = Et + np.exp(1j * omega * td) * np.exp(-1.38 * (td/tau)**2)
            Etdmtrx[(ii),(jj)] = Etd

            aa = (np.abs(Etd))**2
           

            imcol[(ii)] = aa
                        

    return tcol, Etcol, delaycol, Etdmtrx, imcol


