#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 23:01:43 2021

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

import matplotlib.pyplot as plt
import matplotlib.axes as ax
from astropy.io import fits
from astropy.wcs import WCS
#from photutils import DAOStarFinder
#from astropy.stats import mad_std
# https://photutils.readthedocs.io/en/stable/getting_started.html

from numpy.polynomial.polynomial import polyfit
from astropy.stats import sigma_clipped_stats
from photutils.psf import IterativelySubtractedPSFPhotometry
from statistics import mode
from astropy.visualization import simple_norm
from photutils.utils import calc_total_error
from astropy.stats import mad_std
import matplotlib.gridspec as gridspec

import julian
#from datetime import datetime
#from datetime import timedelta
#from datetime import date
import datetime
import subprocess


#file_info='slt_target_fitsheader_info.txt'
#file_info='slt_target_fitsheader_info_exclude_baddata_join.txt'
file_info='./refdb_vizier_mod.txt'
df_info=pd.read_csv(file_info,delimiter=',')
#print(df_info)
#print(df_info['count'])

#print(df_info['name'])
#print(df_info['ra'])
#print(df_info['dec'])
#print(df_info['V_mag'])
#print(df_info['V_mag_Err'])
#print(df_info['R_mag'])
#print(df_info['R_mag_Err'])

df_refstar=df_info.drop(['R:0-1', 'G:0-1', 'B:0-1', 'alpha', 'size', 'band', 'jd', 'count','empty'],axis=1)
#df_refstar=df_info.drop(['alpha'],axis=1)
print(df_refstar)
#print(df_refstar['V_mag'])

df_refstar=df_refstar.drop(['name','I_mag', 'I_mag_Err', 'V_mag', 'V_mag_Err', 'R_mag', 'R_mag_Err'],axis=1)

df_refstar['shape']='circle'
df_refstar['radius']=60
df_refstar=df_refstar[['shape','ra','dec','radius']]
df_refstar.rename(columns={'ra':'ra_deg'},inplace=True)
df_refstar.rename(columns={'dec':'dec_deg'},inplace=True)



#df_refstar['ra_hhmmss']=df_refstar['ra_deg']


print(df_refstar)
 
dir_refstar='refstar/'
file_refstar_reg=dir_refstar+'refstar_radec.reg'
df_refstar.to_csv(file_refstar_reg,sep=',',index=False,header=None)    


subprocess.call(["sed -i 's/circle,/circle(/g' refstar_radec.reg"],shell=True)
subprocess.call(["sed -i 's/60/60\")/g' refstar_radec.reg"],shell=True)



#subprocess.call(["sed -i 's/circle,/circle(/g'", file_refstar_reg],shell=True)
#subprocess.call(["sed -i 's/60/60\")/g'", file_refstar_reg],shell=True)

head1='headlist="# Region file format: DS9 version 4.1'
head2='global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1'
head3='fk5'

subprocess.call(["sed -i '1i fk5' refstar_radec.reg"],shell=True)
subprocess.call(["sed -i '1i global color=green dashlist=8 3 width=1 font=\"helvetica 10 normal roman\" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1' refstar_radec.reg"],shell=True)
subprocess.call(["sed -i '1i # Region file format: DS9 version 4.1' refstar_radec.reg"],shell=True)


