#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 04:48:28 2019

@author: altsai
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

generate master bias, master dark, master flat for one month.
$ condaa
$ python slt_calibration_science_target.py slt201908
or
$ python slt_calibration_science_target.py slt20190822

"""



#dir_root='/home/altsai/project/20190801.NCU.EDEN/data/gasp/'
#dir_root='/home/altsai/gasp/lulin_data/2019/slt/'
#dir_month='slt201908'
#date=dir_month+'22'
#dir_master=dir_month+'_master/'
#dir_calib_sci=date+'_calib_sci/'


import os
import sys
import shutil
#import re
import numpy as np
#import numpy
from astropy.io import fits
#import matplotlib.pyplot as plt
#import scipy.ndimage as snd
#import glob
#import subprocess
#from scipy import interpolate
#from scipy import stats
#from scipy.interpolate import griddata
#from time import gmtime, strftime
import pandas as pd
from datetime import datetime
#from scipy import interpolate
#from scipy import stats



#print("Which Month you are going to process ?")
#yearmonth=input("Enter a year-month (ex: 201908): ")
yearmonth=sys.argv[1]
#yearmonth='202010'
year=str(yearmonth[0:4])
month=str(yearmonth[4:6])

#folder=sys.argv[1]
#folder='slt201908'
dir_month='slt'+yearmonth
#print(dir_month)
dir_master=yearmonth+'/'+dir_month+'_master/'
#dir_master='data/'+yearmonth+'/'+dir_month+'_master/'

print(dir_master)
#dir_calib_sci=date+'_calib_sci/'
#print(dir_calib_sci)

#if os.path.exists(dir_master):
#    shutil.rmtree(dir_master)
#os.makedirs(dir_master,exist_ok=True)

print('...generate master files on '+dir_month+'...')


#dark_time='005S'
#dark_time='010S'
#dark_time='030S'
dark_time=sys.argv[2]

#sys.exit(0)


'''
logfile=dir_month+'_master.log'
sys.stdout=open(logfile,'w')
print(sys.argv)
'''

#time_calib_start=strftime("%Y-%m-%d %H:%M:%S", gmtime())
#time_calib_start=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
time_calib_start=str(datetime.now())  
print('Data calibrated by An-Li Tsai at '+time_calib_start+' UTC')


print(' ---------------------------')
print(' Load Master Bias ')
print(' ---------------------------')

cmd_search_file_bias='find ./ | grep '+dir_master+' | grep fits | grep master_bias'
print(cmd_search_file_bias)
file_bias=os.popen(cmd_search_file_bias,"r").read().splitlines()[0]

#array_each_bias=np.array([pyfits.getdata(i) for i in file_bias])
master_bias=fits.open(file_bias)[0].data
#print(master_bias)
print('...load master bias: '+file_bias+'...')


print(' ---------------------------')
print(' Master Dark (subtract from Bias) ')
print(' ---------------------------')


#dark_time='005S'
#dark_time='010S'
#dark_time='030S'


cmd_search_dark='find ./ |grep '+dir_month+' | grep fts | grep Dark | grep '+dark_time
print(cmd_search_dark)
list_file_dark=os.popen(cmd_search_dark,"r").read().splitlines()
print(list_file_dark)

list_file_dark_px2048=[]
print(list_file_dark_px2048)

#sys.exit(0)

for path_file in list_file_dark:
    hdu=fits.open(path_file)[0]
    imhead=hdu.header
    imdata=hdu.data
    nx1=imhead['NAXIS1']
    nx2=imhead['NAXIS2']
    if nx1 == 2048:
        if nx2 == 2048:
#            print("pixel = ",nx1," x ",nx2)
            list_file_dark_px2038=list_file_dark_px2048.append(path_file)

print(list_file_dark_px2048)

#sys.exit(0)

#print('...start to remove outlier dark...')

#master_dark={}

array_dark=np.array([fits.open(j)[0].data for j in list_file_dark_px2048])
#print('...remove outlier data...')
#dark_keep=reject_outliers_data(array_dark,par1)
#dark_each_time_keep2=reject_outliers_data(dark_each_time_keep,3)
#print(dark_keep)
print('...generate master dark...')
dark_subtract=array_dark-master_bias
mean_dark=np.mean(dark_subtract,axis=0)
#print('...remove outlier pixel...')
#mean_dark_keep=reject_outliers_px(mean_dark,par2)
master_dark=mean_dark
#print('skip this step')
#master_dark[i]=mean_dark_each_time_keep
#print(master_dark_each_time[1000][1000])
#plt.title('Master Dark '+i)
#plt.imshow(master_dark_each_time)
#plt.show()
print('...output master dark '+dark_time+' to fits file...')
fitsname_master_dark='master_dark_'+dark_time+'_'+dir_month+'.fits'
now=str(datetime.now())  
#fits.header.add_history('Master Dark generated at '+now+' UTC')
#hdu=fits.PrimaryHDU(master_dark[i])
hdu=fits.PrimaryHDU(master_dark)
hdu.writeto(dir_master+fitsname_master_dark,overwrite=True)
#now=str(datetime.now())  
#imhead.add_history('Master bias is applied at '+now+' UTC')
#fits.writeto(fitsname_master_dark,data=master_dark_each_time,header=imhead,overwrite=True)

del list_file_dark
del list_file_dark_px2048
del array_dark

print('... finished ...')


