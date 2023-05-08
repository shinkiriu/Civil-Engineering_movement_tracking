# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def plotFreq(paths):
    a = np.array(paths)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
    for i in range(a.shape[1]):
        plt.subplot(a.shape[1], 2, 2*i+1)
        plt.plot(a[:,i,0])
        plt.title(str(i)+"th pos on X")
        
        plt.subplot(a.shape[1], 2, 2*i+2)
        plt.plot(a[:,i,1])
        plt.title(str(i)+"th pos on Y")
    
    