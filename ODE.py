# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 10:15:00 2017

@author: BME_HeLab
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def firstorder(y,t,K,u):
    tau = 5.0
    dydt = (-y + K*u)/tau
    return dydt


t=np.linspace(0,20,17)
K = 2.0
u = 1.0
y0 = 0
y = odeint(firstorder,y0,t,args=(K,u))
plt.plot(t,y)