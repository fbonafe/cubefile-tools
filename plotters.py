# -*- coding: utf-8 -*-
"""
Some plot tools related to CUBE file properties.
"""

import numpy as np
import matplotlib.pyplot as plt
#from scipy.interpolate import griddata
from matplotlib.mlab import griddata

def plotxy(coorx,coory,x,y,z,filename):
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    coorx = np.array(coorx)
    coory = np.array(coory)    
    npts=500
    
    xi = np.linspace(x.min(),x.max(),npts)
    yi = np.linspace(y.min(),y.max(),npts)
    zi = griddata(x, y, z, xi, yi, interp='linear')
    maxdim = max(np.abs(x).max(),np.abs(y).max())
    densmax = np.abs(z).max()/2
    dbond = 1.5
    
    figure = plt.figure(figsize=(20, 16))
    figure = plt.xlim(-maxdim,maxdim)
    figure = plt.ylim(-maxdim,maxdim)
    figure = plt.contourf(xi,yi,zi,100,cmap=plt.cm.seismic,vmax=densmax,vmin=-densmax)
    for i in range(coorx.shape[0]):
        for j in range(coory.shape[0]):
            dreal = np.sqrt((coorx[j]-coorx[i])**2+(coory[j]-coory[i])**2)
            if dreal <= dbond:
                figure = plt.plot([coorx[i],coorx[j]],[coory[i],coory[j]], color="0.5", lw=1.5)
    #plt.contour(xi,yi,zi,15,linewidths=0.5,colors='k')    
    #plt.ylabel('y / $\AA$', fontsize=18)
    #plt.xlabel('x / $\AA$', fontsize=18)
    figure = plt.axis('off')
    cbar = plt.colorbar()
    cbar.ax.tick_params(labelsize=30) 
    figure = plt.savefig(filename+'.eps')
    #clb.ax.set_ylabel('electrostatic potential / $V$', fontsize=18)
    return figure
