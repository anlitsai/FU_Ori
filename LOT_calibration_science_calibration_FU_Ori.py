#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:54:00 2019

@author: altsai
"""

"""
Spyder Editor

data calibration for science target.
$ condaa
$ python LOT_calibration_science_target.py _FOLDER_NAME_

for example:
$ python LOT_calibration_science_target.py LOT20190822
"""

dir_root='/home/altsai/project/20190801.NCU.EDEN/data/gasp/'
#dir_root='/home/altsai/gasp/lulin_data/2019/LOT/'

import os
import sys
import shutil
#import re
import numpy as np
#import numpy
from astropy.io import fits
#import pyfits
import matplotlib.pyplot as plt
#import scipy.ndimage as snd
#import glob
#import subprocess
#from scipy import interpolate
#from scipy import stats
#from scipy.interpolate import griddata
#from time import gmtime, strftime
#import pandas as pd
from datetime import datetime

yearmonth='202010'
year=str(yearmonth[0:4])
month=str(yearmonth[4:6])

dir_month='LOT'+yearmonth

dir_master=yearmonth+'/LOT'+yearmonth+'_master/'
#dir_master='data/'+yearmonth+'/LOT'+yearmonth+'_master/'
print(dir_master)

cmd_search_folder='find ./'+yearmonth+'/ | grep '+dir_month+'[0-9][0-9]$ |cut -d / -f3|sort|uniq'
print(cmd_search_folder)
#list_folder=os.popen(cmd_search_folder,"r").read().splitlines()[0]
list_folder=os.popen(cmd_search_folder,"r").read().splitlines()
print(list_folder)

dir_calib_sci=yearmonth+'/LOT'+yearmonth+'_calib_sci/'

print(dir_calib_sci)
if os.path.exists(dir_calib_sci):
    shutil.rmtree(dir_calib_sci)
os.makedirs(dir_calib_sci,exist_ok=True)

#print('... will calibrate science target on '+date+' ...')

#sys.exit(0)

'''
logfile=folder+'_sci.log'
sys.stdout=open(logfile,'w')
print(sys.argv)
'''

#time_calib_start=strftime("%Y-%m-%d %H:%M:%S", gmtime())
#time_calib_start=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
time_calib_start=str(datetime.now())  
print('Data calibrated by An-Li Tsai at '+time_calib_start+' UTC+8')
#print('')

print(' ---------------------------')
print(' Load Master Bias ')
print(' ---------------------------')

cmd_search_file_bias='find ./ | grep '+dir_master+' | grep fits | grep master_bias'
print(cmd_search_file_bias)
file_bias=os.popen(cmd_search_file_bias,"r").read().splitlines()[0]
print('BIAS file:', file_bias)
#sys.exit(0)

master_bias=fits.open(file_bias)[0].data
#print(master_bias)
print('...load master bias: '+file_bias+'...')

#sys.exit(0)


print(' ---------------------------')
print(' Load Master Dark ')
print(' ---------------------------')

cmd_search_file_dark='find ./ | grep '+dir_master+' | grep fits | grep master_dark'
print(cmd_search_file_dark)
list_file_dark=os.popen(cmd_search_file_dark,"r").read().splitlines()
print('list DARK files:',list_file_dark)
n_file_dark=len(list_file_dark)
print('# of DARK files:', n_file_dark)

#master_dark=fits.open(file_dark)[0].data

#sys.exit(0)

print(' ---------------------------')
print(' Science Target ')
print(' ---------------------------')

print(dir_month)
cmd_search_file_sci="find ./ | grep "+dir_month+" | grep 'fts\|new' | grep FU_Ori "
print(cmd_search_file_sci)
list_file_sci=os.popen(cmd_search_file_sci,"r").read().splitlines()
print('list SCI files:', list_file_sci)
n_file_sci=len(list_file_sci)
print('# of SCI files', n_file_sci)
print('...calibrating science targets...')

#sys.exit(0)

#calib_sci={}

for i in list_file_sci:
    print('file to be calibrated: ', i)
    hdu=fits.open(i)[0]
    imhead=hdu.header
    imdata=hdu.data
#    print(imdata.shape)
    exptime=imhead['EXPTIME']
    idx_time=str(int(exptime))+'S'
    print('exposure time : ', idx_time)
#    naxis=imhead['NAXIS']
#    print(naxis)
    jd=imhead['JD']
    obj=imhead['OBJECT']
    try:
        fwhm=imhead['FWHM']
    except:
        fwhm=-9999
    try:
        zmag=imhead['ZMAG']
    except:
        zmag=-9999
    airmass=imhead['AIRMASS']
    altitude=imhead['ALTITUDE']
    ra=imhead['RA']
    dec=imhead['Dec']
    filter_name=imhead['FILTER']    

    print('... load master dark ...')    
    cmd_search_file_dark='find ./'+dir_master+' | grep fits | grep master_dark|grep '+idx_time
    print(cmd_search_file_dark)
    file_master_dark=os.popen(cmd_search_file_dark,"r").read().splitlines()[0]
    print('selected DARK file:', file_master_dark)

    data_dark=fits.open(file_master_dark)[0].data

    select_master_dark=data_dark
#    print('dark file : ', select_master_dark)

    print('... load master flat ...')
#    print(cmd_search_file_flat)
    #cmd_sci_filter='echo '+filter_name+' | cut -d _ -f1'
    sci_filter=filter_name.split('_',-1)[0]
    print('science filter : ', sci_filter)
#    cmd_search_file_flat='find ./ | grep '+dir_master+' | grep '+sci_filter
    cmd_search_file_flat_filter='find ./'+dir_master+' | grep fits | grep master_flat|grep '+sci_filter
    print(cmd_search_file_flat_filter)
    file_flat_filter=os.popen(cmd_search_file_flat_filter,"r").read().splitlines()[0]
    print('selected FLAT file : ', file_flat_filter)

    print('... master flat file is: '+file_flat_filter+' ...')

    data_flat=fits.open(file_flat_filter)[0].data
    select_master_flat=data_flat
    sci_flat=(imdata-master_bias-select_master_dark)/select_master_flat
    cmd_sci_name='echo '+i+' | cut -d / -f5 | cut -d . -f1'
    print(cmd_sci_name)
    sci_name=os.popen(cmd_sci_name,"r").read().splitlines()[0]
#    print(sci_name)
#    plt.title(sci_name)
#    plt.imshow(sci_flat,cmap='rainbow')
#    plt.show()
    print('...output calibrated '+sci_name+' to fits file...')
    time_calib=str(datetime.now())  
    imhead.add_history('Master bias, dark, flat are applied at '+time_calib+' UTC+8 by An-Li Tsai')
    fitsname_calib_sci=sci_name+'_calib.fits'
    #hdu=fits.PrimaryHDU(calib_sci[i])
    fits.writeto(dir_calib_sci+fitsname_calib_sci,data=sci_flat,header=imhead,overwrite=True)
    print(' ')
    
#sys.exit(0)


print('---------------------------')

time_calib=str(datetime.now())
print('...finish calibration at '+time_calib+' UTC+8...')
print()


