# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:57:30 2015

@author: eric.bertok
"""

import scipy.integrate as sp
import matplotlib.pyplot as plt
import numpy as np
import time


#Parameters:
omega=1
N=2000

#Set Diff. Equation:
def Sys(t,X):
    return np.array([X[1],-omega**2*np.sin(X[0])])

#integrationsfunktion:
def integrate(q,p,dt=0.5):
    global result    
    global fig
    global N
    r=[]
    
    for n in range(0,N):
        r.append(sp.ode(Sys))
        r[n].set_integrator('dopri5')
        r[n].set_initial_value([q[n],p[n]])      
        if n==N:
            break  
     
    plt.plot(q,p,'o',ms=0.2)        
    while r[0].t<1000:
        for n in range(0,N):
            result[n]=r[n].integrate(r[n].t+dt)     
        if r[0].t==10:
            print 'YAAAY'
            np.savetxt('t=10.dat',result)
        if r[0].t==50:
            print 'YAAAY'
            np.savetxt('t=50.dat',result)
        if r[0].t==250:
            print 'YAAAY'
            np.savetxt('t=250.dat',result)
        if r[0].t==500:
            print 'YAAAY'
            np.savetxt('t=500.dat',result)
        if r[0].t==1000:
            print 'YAAAY'
            np.savetxt('t=1000.dat',result)
            
#Gibbs Ensamble:
def gibbs(q_0=1,p_0=1,R=0.2):
    global N
    global u
    q=np.zeros(N)
    p=np.zeros(N)
    for n in range(0,N):
        q[n]=q_0-R+2*R*np.random.rand()
        p[n]=p_0+np.sqrt(R**2-(q[n]-q_0)**2)*(2*np.random.rand()-1)  
    u=np.vstack((q,p))
    u=u.T
    print u
    np.savetxt('t=0.dat',u)
    return q,p
    
start = time.time()

result=np.zeros((N,2))
fig=plt.figure()
q,p=gibbs(q_0=1,p_0=1,R=0.2)
integrate(q,p)

	
stop = time.time()
print stop-start,'\t'

#plt.colorbar()


    