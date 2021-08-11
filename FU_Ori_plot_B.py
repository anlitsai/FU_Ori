#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:15:21 2020

@author: altsai
"""


#import os
#import sys
#import shutil
import numpy as np
#import csv
#import time
#import math
import pandas as pd
import matplotlib.pyplot as plt

obj_name='FU Ori'
filter_ID=['B']
#list_data=['./slt_InstMag_Vmag/Vmag_FU_Ori_all.txt']
list_data=['./slt_InstMag_Bmag_AAVOS_ABCDEI/Bmag_FU_Ori_all.txt']
filter_mag=['Bmag']
filter_err=['ErrorBmag']

n_data=len(list_data)

#fig,axs=plt.subplots(3,1,figsize=(6,8))
#fig,axs=plt.subplots(2,1,figsize=(6,8))
fig,axs=plt.subplots(1,1,figsize=(8,6))
fig.subplots_adjust(hspace=0.5,wspace=0.5)
#axs=axs.ravel()

for i in range(n_data):
    file_data=list_data[i]
    print('data file: ',file_data)
    
#    w1_file='dat_file/g'+file_dat[0:4]+'r_LuS_20180401-now.dat'
#    df_w1=pd.read_csv(w1_file,delim_whitespace=True,header=None,usecols=[0,1,2]) 
    df_data=pd.read_csv(file_data) #,secols=[1,2,3]) 
    print(df_data)

    JD=df_data['JD'].map('{:.5f}'.format).astype(np.float64)
#    print(JD1)
    Mag=df_data[filter_mag[i]]
#    print(R1)
    err=df_data[filter_err[i]]
#    print(eR1)
    

#    axs[i].errorbar(JD0,R0,yerr=eR0,linestyle='--',label='no w',lw=1)
    axs.errorbar(JD,Mag,yerr=err,linestyle='--',lw=1)  
    axs.set_xlabel('JD')
    axs.set_ylabel(filter_mag[i])
    axs.set_title(obj_name)
    axs.invert_yaxis()
#    axs[i].legend(loc='best')
    


plt.savefig('FU_Ori_plot_B.pdf') 
plt.savefig('FU_Ori_plot_B.png') 

print("... save file as FU_Ori_plot_B.pdf ...")

