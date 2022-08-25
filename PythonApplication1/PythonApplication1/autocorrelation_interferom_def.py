
# autocorrelation_interferom_def.py

import numpy as np

def proc1(freq=8,pulsewidth=0.4,m=256,steptime=0.025):

    tcol = np.zeros((m,1)); # time
    
    Etcol = np.ones(m, dtype=complex);#*2
       
    Signalcol = np.ones(m, dtype=complex);#*2

    omega = 2*np.pi*freq
 
    print('omega=', omega, 'Hz')


    # PD signal. Proportional to optical power
    #Signal = 0


    for ii in range(m):

        delay1 = steptime*ii-0.5*steptime*m   

        s = 0
        
        for jj in range(m):

            time1 = steptime*jj-0.5*steptime*m
            tcol[(jj)] = time1
            
            Et = np.exp(1j * omega * time1) * np.exp(-1.38 * (time1/pulsewidth)**2)
            
            Etcol[(jj)] = Et
            
            #Et = math.sin(omega * time1)     

            td = time1 + delay1

            Etd = np.exp(1j * omega * td) * np.exp(-1.38 * (td/pulsewidth)**2)                          

            s += (abs(Et+Etd)**2)**2            

              #Signalcol[(ii)] = Etd
            Signalcol[(ii)] = s

    return tcol, Etcol,Signalcol

#End of File