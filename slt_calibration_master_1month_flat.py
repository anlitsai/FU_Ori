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
print(' Master Flat (subtract from Dark and Bias) ')
print(' ---------------------------')

#os.chdir(dir_date+"/flat/")
#cmd_search_sci_filter="find ./ |grep "+dir_month+" | grep GASP | cut -d / -f6 | grep fts|cut -d '@' -f2 | cut -d _ -f1 | cut -d - -f2 | sort | uniq"

#print(cmd_search_sci_filter)
#list_flat_filter=os.popen(cmd_search_sci_filter,"r").read().splitlines()
#print('all filter: ',list_flat_filter)

#list_flat_filter=['R']
#for i in list_flat_filter:
#    print('filter',i)


#sys.exit(0)

list_index_flat_dark=['V_10','B_30','R_5']

#list_flat_filter=['V','B','R']


master_flat={}
#print(master_flat)
#awk -F'PANoRot-' '{print $2}'|cut -d _ -f1
#for flat_filter in list_flat_filter:
for index_flat_dark in list_index_flat_dark:
    print("index flat_dark = ", index_flat_dark)
    #flat_filter=(list_index_flat_dark[flat_dark].split("_",-1)[0])
    index_flat_filter=index_flat_dark.split("_",-1)[0]
    print("index flat = ",index_flat_filter)
    index_dark_time=index_flat_dark.split("_",-1)[1]
    print("index dark = ",index_dark_time,"S")
    #dark_time=(list_index_flat_dark[flat_dark].split("_",-1)[1])
    cmd_search_file_flat='find ./ |grep '+dir_month+' | grep fts | grep flat | grep Bin1| grep PANoRot-'+index_flat_filter
    print(cmd_search_file_flat)
    list_file_flat=os.popen(cmd_search_file_flat,"r").read().splitlines()
    print('file list',list_file_flat)
    #print(len(list_file_flat))
    #array_flat=np.array([pyfits.getdata(j) for j in list_file_flat])
    array_flat=np.array([fits.open(j)[0].data for j in list_file_flat])
#    print(array_flat.shape)
#    print('...remove outlier data...')
#    flat_keep=reject_outliers_at_same_px(array_flat)
#    flat_keep2=reject_outliers_data(flat_keep,par2)
    print(' ---------------------------')
    print(' Load Master Dark ')
    print(' ---------------------------')
    cmd_search_file_dark='find ./ |grep '+dir_month+' | grep fits | grep master_dark | grep '+index_dark_time
    print("cmd_search_file_dark = ", cmd_search_file_dark)
    list_file_dark=os.popen(cmd_search_file_dark,"r").read().splitlines()
    print("list_file_dark = ",list_file_dark)
    data=fits.open(list_file_dark[0])[0].data
    print(data)
    master_dark=data
    print(' ---------------------------')
    print(' Master Dark Loaded')
    print(' ---------------------------')
#    print('--------')
    print('...generate master flat '+index_flat_filter+'...')
    print('master bias: ', master_bias.shape)
    print('master dark: ', master_dark.shape)
    print('array flat: ',array_flat.shape) 
#    mean_flat=np.nanmean(flat_keep-master_bias-master_dark,axis=0)  
    mean_flat=np.mean(array_flat,axis=0)  
#        print(np.amax(mean_flat_each_filter))
#    print('...remove outlier pixel...')
#    mean_flat_keep=reject_outliers2_px(mean_flat,par3)
    min_value_flat=np.nanmin(mean_flat)
    max_value_flat=np.nanmax(mean_flat)
    mean_value_flat=np.mean(mean_flat)
    print('min, max =',min_value_flat,max_value_flat)
    flat_subtract=mean_flat-master_bias-master_dark
    #norm_mean_flat=(mean_flat-min_value)/(max_value-min_value)
#    flat_subtract=mean_flat-master_bias-master_dark
#    norm_mean_flat=(mean_flat-min_value)/(max_value-min_value)  #max_value
    norm_mean_flat=mean_flat/mean_value_flat  #normalized to mean value
#        print(np.amax(norm_mean_flat_each_filter))
    master_flat[index_flat_filter]=norm_mean_flat
#        print(master_flat[idx_filter_time])
#    print(mean_flat_each_filter[1000][1000])
#    plt.title('Master Flat '+i)
#    plt.imshow(mean_flat_each_filter)
#    plt.show()
    print('...output master flat '+index_flat_filter+' to fits file...')
#    fitsname_master_flat='master_flat_'+flat_filter+'_180S_'+dir_month+'.fits'
    fitsname_master_flat='master_flat_'+index_flat_filter+'_'+dir_month+'.fits'
    hdu=fits.PrimaryHDU(master_flat[index_flat_filter])
#        now=str(datetime.now())  
#        fits.header.add_history('Master Flat generated at '+now+' UTC')
    hdu.writeto(dir_master+fitsname_master_flat,overwrite=True)
#        imhead.add_history('Master bias, dark are applied at '+now+' UTC')
#        fits.writeto(fitsname_master_flat,data=norm_mean_flat_each_filter,header=imhead,overwrite=True)

del list_file_dark
del list_index_flat_dark
#del list_flat_filter
del list_file_flat
del array_flat

print('... finished ...')


