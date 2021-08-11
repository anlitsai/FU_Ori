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
$ python slt_calibration_science_target.py _FOLDER_NAME_

for example:
$ python slt_calibration_science_target.py slt20190822
"""

dir_root='/home/altsai/project/20190801.NCU.EDEN/data/gasp/'
#dir_root='/home/altsai/gasp/lulin_data/2019/slt/'

#folder='slt201908'
#date=month+'22'
#dir_master=folder+'_master/'
#dir_calib_sci=date+'_calib_sci/'

#print(month,date)

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

print()
print('format: python check_exposure_time.py slt20201010')
print()

folder=sys.argv[1]
#folder='slt20191201'
#print("Which Folder you are going to process ?")
#folder=input("Enter a Folder (ex: slt20190822): ")
date=folder[3:]
year=str(date[0:4])
month=str(date[4:6])
yearmonth=year+month
day=str(date[6:8])
#folder='slt'+date
dir_folder=yearmonth+'/'+folder+'/'




dir_sci=yearmonth+'/'+folder+'/'

#dir_calib_sci=yearmonth+'/'+folder+'_calib_sci/'
#dir_calib_sci='data/'+yearmonth+'/'+folder+'_calib_sci/'

print(dir_sci)



#sys.exit(0)



print(' ---------------------------')
print(' Science Target ')
print(' ---------------------------')

print(folder)
#cmd_search_file_sci="find ./ | grep "+dir_folder+" | grep fts | grep GASP "
cmd_search_file_sci="find ./ | grep "+dir_folder+" | grep 'fts\|new' | grep GASP "
list_file_sci=os.popen(cmd_search_file_sci,"r").read().splitlines()
print('...check exposure time of science targets...')
#print(list_file_sci)
print(len(list_file_sci))
#sys.exit(0)

#cmd_search_sci_filter="find ./ |grep "+date" | grep fts |grep GASP | cut -d / -f4 | awk -F'_Astro' '{print $1}'| rev | cut -c1-3 | rev | cut -d - -f2 "

#os.chdir(dir_root+"wchen/wchen_03_GASP_01/")

#cmd_sci1="ls ./ | awk -F'_Astrodon' '{print $1}'| awk '{print substr($0,length-2,3)}' | cut -d - -f2 |sort |uniq"
#print(sci_filter_list)

#sci_list=os.popen("ls","r").read().splitlines()
#print(sci_list)

#calib_sci={}

for i in list_file_sci:
    hdu=fits.open(i)[0]
    imhead=hdu.header
    imdata=hdu.data
#    print(imdata.shape)
    exptime=imhead['EXPTIME']
    idx_time=str(int(exptime))+'S'
#    print(idx_time)
#    print(exptime)
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

    print(i, "\t", idx_time)
    
#sys.exit(0)


print(' ---------------------------')

print()


