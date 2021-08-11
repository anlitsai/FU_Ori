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

if os.path.exists(dir_master):
    shutil.rmtree(dir_master)
os.makedirs(dir_master,exist_ok=True)

print('...generate master files on '+dir_month+'...')

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
print(' Master Bias (mean) ')
print(' ---------------------------')


array_each_bias=[]

#cmd_search_file_bias='find ./ |grep '+dir_month+' | grep fts | grep Bias'
cmd_search_file_bias='find ./'+yearmonth+'/|grep '+dir_month+' | grep fts | grep Bias'
list_file_bias=os.popen(cmd_search_file_bias,"r").read().splitlines()
print(list_file_bias)
n_bias=len(list_file_bias)
print('number of total bias:',n_bias)
#sys.exit(0)
#array_each_bias=np.array([pyfits.getdata(i) for i in list_file_bias])
#array_each_bias=np.array([fits.open(i)[0].data for i in list_file_bias])
n_bias_2048=0
for i in range(n_bias):
    j=list_file_bias[i]
#    print(j)
    imdata=fits.open(j)[0].data
    imhead=fits.open(j)[0].header
    nx=imhead['NAXIS1']
#    print('NAXIS1',nx)
    if nx==2048:
        array_each_bias.append(imdata)
        n_bias_2048=n_bias_2048+1
array_each_bias=np.array(array_each_bias,dtype=int)
print(array_each_bias)
#print(type(array_each_bias))

del list_file_bias

print('number of selected bias:',n_bias_2048)

#print(array_each_bias.shape)
#n_arr_bias=(array_each_bias.shape[0])
#n_arr_bias=len(array_each_bias)
print('number of total px: 2048x2048x',n_bias_2048,' = ', 2048*2048*n_bias_2048)

#sys.exit(0)

print('...generate master bias...')

mean_bias=np.mean(array_each_bias, axis=0)
print(mean_bias.shape)
print(mean_bias)

del array_each_bias


master_bias=mean_bias #_keep
print(master_bias)
print('min,max, mean', np.nanmin(master_bias),np.nanmax(master_bias), np.nanmean(master_bias))
#plt.title('Master Bias')
#plt.imshow(master_bias)
#plt.show()

print('...output master bias to fits file...')

fitsname_master_bias='master_bias_'+dir_month+'.fits'
hdu=fits.PrimaryHDU(data=master_bias)
#hdr=fits.Header()
#now=str(datetime.now())  
#hdr.add_history('Master Bias generated at '+now+' UTC')
#hdu._writeheader('Master Bias generated at '+now+' UTC')
hdu.writeto(dir_master+fitsname_master_bias,overwrite=True)
#now=str(datetime.now())  
#imhead.add_history('Master bias is generated at '+now+' UTC')
#fits.writeto(fitsname_master_bias,data=master_bias,header=imhead,overwrite=True)

#sys.exit(0)


print('... finished ...')


