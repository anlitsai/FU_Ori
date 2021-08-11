#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:52:01 2021

@author: altsai
"""
import os
import sys
import shutil
import numpy as np
import csv
import time
import math
import pandas as pd
from astropy import units as u
from astropy.coordinates import SkyCoord  # High-level coordinates
#from astropy.coordinates import ICRS, Galactic, FK4, FK5 # Low-level frames
#from astropy.coordinates import Angle, Latitude, Longitude  # Angles
#from astropy.coordinates import match_coordinates_sky
from astropy.table import Table
from photutils import CircularAperture
from photutils import SkyCircularAperture
from photutils import aperture_photometry
from photutils import CircularAnnulus
from photutils import SkyCircularAnnulus
# https://photutils.readthedocs.io/en/stable/aperture.html
#from phot import aperphot
# http://www.mit.edu/~iancross/python/phot.html
from astropy.stats import SigmaClip
from photutils.background import Background2D, MedianBackground
#https://photutils.readthedocs.io/en/stable/background.html

import matplotlib.pyplot as plt
import matplotlib.axes as ax
from astropy.io import fits
from astropy.wcs import WCS
#from photutils import DAOStarFinder
#from astropy.stats import mad_std
# https://photutils.readthedocs.io/en/stable/getting_started.html

from numpy.polynomial.polynomial import polyfit
#from astropy.stats import sigma_clipped_stats
#from photutils.psf import IterativelySubtractedPSFPhotometry
#from statistics import mode
#from astropy.visualization import simple_norm
#from photutils.utils import calc_total_error
#from astropy.stats import mad_std
#import matplotlib.gridspec as gridspec

import julian
#from datetime import datetime
#from datetime import timedelta
#from datetime import date
import datetime
from matplotlib import colors
print("start")
path='nowt/'
#file='/home/altsai/project/20190801.NCU.Prof.Chen/data/fuori/CN_data_some/nowt/Fu_Ori_B_20201018224720_6s_0764_wcs.fits'
file='Fu_Ori_B_20201018224720_6s_0764_wcs.fits'
path_file=path+file
print("filename",path_file)
file_root=file.split('.',-1)[0]
print(file_root)

hdu=fits.open(path_file)[0]
imhead=hdu.header
imdata=hdu.data    
#wcs = WCS(imhead)

#print("imhead")
#print(imhead)
#print("imdata")
#print(imdata)
#print("done")

nx=int(imhead['NAXIS1'])
print("nx = ",nx)
nx_half=int(nx/2)
print(nx_half)

ny=int(imhead['NAXIS2'])
print("ny = ", ny)
ny_half=int(ny/2)
print(ny_half)

value_max=550
value_min=450
#print(imdata[1,1000])
#print(imdata[1,n_half])
#print(imdata[10,])
#print(imdata[1500,1:100])   
#print(imdata[1500,1000:1100])   
#print(imdata[1500,2000:2064])   

#colormap = colors.ListedColormap(["darkblue","lightblue"])
fig=plt.figure(figsize=(8,6))
#plt.imshow(imdata,cmap=colormap)
#plt.imshow(imdata,alpha=0.75)
#plt.imshow(imdata,cmap='hot')
#plt.imshow(imdata,cmap='viridis')
plt.imshow(imdata,vmin=value_min,vmax=value_max,cmap='viridis')
plt.title("imdata")
plt.colorbar()
plt.show()


n_vertical_mid=1000
n_vertical_end=1999+1
n_horizontal_mid=1001-1
n_horizontal_end=2000

plt.imshow(imdata[0:n_vertical_end,0:n_horizontal_end],vmin=value_min,vmax=value_max,cmap='viridis')
plt.title("imdata")
plt.colorbar()
plt.show()


imdata1=imdata[0:n_vertical_mid,0:n_horizontal_mid]
#plt.imshow(imdata1,vmin=value_min,vmax=value_max,cmap='viridis')
#plt.title("imdata1")
#plt.colorbar()
#plt.show()

imdata2=imdata[n_vertical_mid:,0:n_horizontal_mid]
#plt.imshow(imdata2,vmin=value_min,vmax=value_max,cmap='viridis')
#plt.title("imdata2")
#plt.colorbar()
#plt.show()

#imdata3=imdata[0:n_vertical_mid,n_horizontal_mid:n_horizontal_end]
imdata3=imdata[0:n_vertical_mid,n_horizontal_mid:]

#plt.imshow(imdata3,vmin=value_min,vmax=value_max,cmap='viridis')
#plt.title("imdata3")
#plt.colorbar()
#plt.show()

#imdata4=imdata[n_vertical_mid:,n_horizontal_mid:n_horizontal_end]
imdata4=imdata[n_vertical_mid:,n_horizontal_mid:]
#plt.imshow(imdata4,vmin=value_min,vmax=value_max,cmap='viridis')
#plt.title("imdata4")
#plt.colorbar()
#plt.show()
#print(imdata4)


#print(imdata[10,998:1003])   
#print(imdata[997:1003,1200])   
#print(imdata[10,1995:])   
#print(imdata[1995:,10])   

#print(np.nanmean(np.array(imdata1)))
#print(np.nanmean(np.array(imdata2)))
#print(np.nanmean(np.array(imdata3)))
#print(np.mean(np.array(imdata4)))
#print(np.nanmean(np.array(imdata4)))
#print(np.median(np.array(imdata4)))


sigma_clip = SigmaClip(sigma=3.)
bkg_estimator = MedianBackground()

bkg1 = Background2D(imdata1, imdata1.shape, filter_size=(3, 3), sigma_clip=sigma_clip, bkg_estimator=bkg_estimator)
print('bkg1.background_median = ',bkg1.background_median)  
print('bkg1.background_rms_median = ',bkg1.background_rms_median)  

bkg2 = Background2D(imdata2, imdata2.shape, filter_size=(3, 3), sigma_clip=sigma_clip, bkg_estimator=bkg_estimator)
print('bkg2.background_median = ',bkg2.background_median)  
print('bkg2.background_rms_median = ',bkg2.background_rms_median)  

bkg3 = Background2D(imdata3, imdata3.shape, filter_size=(3, 3), sigma_clip=sigma_clip, bkg_estimator=bkg_estimator)
print('bkg3.background_median = ',bkg3.background_median)  
print('bkg3.background_rms_median = ',bkg3.background_rms_median)  

bkg4 = Background2D(imdata4, imdata4.shape, filter_size=(3, 3), sigma_clip=sigma_clip, bkg_estimator=bkg_estimator)
print('bkg4.background_median = ',bkg4.background_median)  
print('bkg4.background_rms_median = ',bkg4.background_rms_median)  

#plt.imshow(bkg4.background, origin='lower', cmap='Greys_r',  interpolation='nearest',vmin=value_min,vmax=value_max)
#plt.colorbar()
#plt.show()

#plt.imshow(imdata4 - bkg4.background, origin='lower',    cmap='Greys_r', interpolation='nearest',vmin=value_min,vmax=value_max)
#plt.colorbar()
#plt.show()

bkg_min=min(bkg1.background_median,bkg2.background_median,bkg3.background_median,bkg4.background_median)

bkg_del=np.array([0.]*4)
bkg_del=(bkg1.background_median,bkg2.background_median,bkg3.background_median,bkg4.background_median)-bkg_min
print(bkg_del)

imdata[0:n_vertical_mid,0:n_horizontal_mid]=imdata[0:n_vertical_mid,0:n_horizontal_mid]-bkg_del[0]
imdata[n_vertical_mid:,0:n_horizontal_mid]=imdata[n_vertical_mid:,0:n_horizontal_mid]-bkg_del[1]
#imdata[0:n_vertical_mid,n_horizontal_mid:n_horizontal_end]=imdata[0:n_vertical_mid,n_horizontal_mid:n_horizontal_end]-bkg_del[2]
#imdata[n_vertical_mid:,n_horizontal_mid:n_horizontal_end]=imdata[n_vertical_mid:,n_horizontal_mid:n_horizontal_end]-bkg_del[3]
imdata[0:n_vertical_mid,n_horizontal_mid:]=imdata[0:n_vertical_mid,n_horizontal_mid:]-bkg_del[2]
imdata[n_vertical_mid:,n_horizontal_mid:]=imdata[n_vertical_mid:,n_horizontal_mid:]-bkg_del[3]

#plt.imshow(imdata[0:n_vertical_end,0:n_horizontal_end],vmin=value_min,vmax=value_max,cmap='viridis')
imdata_cut=imdata[0:n_vertical_end,0:n_horizontal_end]

plt.imshow(imdata,vmin=value_min,vmax=value_max,cmap='viridis')
plt.title("imdata")
plt.colorbar()
plt.show()

path_file_bg_flatten=path+file_root+'_bg_flatten.fits'
#hdu=fits.PrimaryHDU(calib_sci[i])
fits.writeto(path_file_bg_flatten,data=imdata_cut,header=imhead,overwrite=True)
