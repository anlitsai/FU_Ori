#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  30 15:18:28 2019

@author: altsai
"""

"""
Spyder Editor

"""
import os
import sys
import numpy as np
import pandas as pd

df01=pd.read_csv('slt_target_fitsheader_info_exclude_baddata_202010.txt',sep='|')
df02=pd.read_csv('slt_target_fitsheader_info_exclude_baddata_202011.txt',sep='|')
df03=pd.read_csv('slt_target_fitsheader_info_exclude_baddata_202012.txt',sep='|')
df04=pd.read_csv('slt_target_fitsheader_info_exclude_baddata_202101.txt',sep='|')
df05=pd.read_csv('slt_target_fitsheader_info_exclude_baddata_202102.txt',sep='|')
df06=pd.read_csv('slt_target_fitsheader_info_exclude_baddata_202103.txt',sep='|')
df07=pd.read_csv('slt_target_fitsheader_info_exclude_baddata_202104.txt',sep='|')

df_all=pd.concat([df01,df02,df03,df04,df05,df06,df07]).reset_index(drop=True)
#print(df_all)
#print(df_all.ID)

#sys.exit(0)
#idx=df_all.values
idx=df_all.index.values
#print(idx)
#sys.exit(0)

ID=idx+1
#print(ID)
#sys.exit(0)

df_out=df_all
#df_out.col_ID=ID
#print(df_out.col_ID)
df_out[df_out.columns[0]]=ID
#print(df_out[df_out.columns[0]])
#sys.exit(0)

print(df_out)

file_join='slt_target_fitsheader_info_exclude_baddata_join.txt'

df_out.to_csv(file_join,sep='|',index=False)

cmd_replace_head='find ./|grep calib | grep slt201908[1-3][0-9]| cut -d / -f3 | sort |uniq'
list_file_sci1=os.popen(cmd_replace_head,"r").read().splitlines()



print('')
print('... join all table files to '+file_join+' ...')
print('')


