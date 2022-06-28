
# autocorrelation_interferom_def.py

import numpy as np


def proc1(param=0.01,m=256):


    tcol = np.zeros((m,1)); # time
    
    Etcol = np.ones(m, dtype=complex)*2

    #Signalcol = np.zeros(m,dtype=complex); #% 
       
    Signalcol = np.ones(m, dtype=complex)*2

    #Etdmtrx = np.ones((m,m), dtype=complex); #% 

    freq = 2
    omega = 2*np.pi*freq
 
    print('omega=', omega, 'Hz')

    #Pulsewidth
    tau = 0.8 

    # PD signal. Proportional to optical power
    #Signal = 0


    for ii in range(m):

        time1 = 0.025*ii-3.2

            

        for jj in range(m):

            tcol[(ii)] = time1

            Et = np.exp(1j * omega * time1) * np.exp(-1.38 * (time1/tau)**2)
            Etcol[(ii)] = Et

            #Et = math.sin(omega * time1)     

            delay1 = 0.025 * jj -4.8      

            td = time1 + delay1

            Etd = Et * np.exp(1j * omega * td) * np.exp(-1.38 * (td/tau)**2)                            
     

            s = 0 
            for kk in range(m):          


                s += Etd
                

                #Signalcol[(ii)] = Etd
                Signalcol[(ii)] = s

            #print(Signalcol)

    return tcol, Etcol,Signalcol


