
yearmonth='202104'
dark_time='010S'
a=`find ./ |grep slt|grep Dark|grep fts|grep $dark_time|grep $yearmonth`
for i in $a; do python check_exposure_pixel_file.py $i;done | tee check_exposure_pixel_slt_Dark_"$dark_time"_"$yearmonth".log

#for i in $a; do python check_exposure_pixel_file.py $i;done | tee check_exposure_pixel_slt_Dark.log

a=`find ./ |grep slt|grep Bias|grep fts`
for i in $a; do python check_exposure_pixel_file.py $i;done | tee check_exposure_pixel_slt_Bias.log


yearmonth='202104'
filter='R_'
a=`find ./ |grep slt|grep Flat|grep fts|grep $filter|grep $yearmonth`
for i in $a; do python check_exposure_pixel_file.py $i;done | tee check_exposure_pixel_slt_Flat_"$filter$yearmonth".log

a=`find ./ |grep slt|grep FU|grep fts`
for i in $a; do python check_exposure_pixel_file.py $i;done | tee check_exposure_pixel_slt_FUOri.log


#a=`find ./ |grep LOT|grep Dark|grep fts`
#for i in $a; do python check_exposure_pixel_file.py $i;done | tee check_exposure_pixel_LOT_Dark.log

#a=`find ./ |grep LOT|grep Bias|grep fts`
#for i in $a; do python check_exposure_pixel_file.py $i;done | tee check_exposure_pixel_LOT_Bias.log

#a=`find ./ |grep LOT|grep flat|grep fits`
#for i in $a; do python check_exposure_pixel_file.py $i;done | tee check_exposure_pixel_LOT_flat.log

#a=`find ./ |grep LOT|grep FU|grep fts`
#for i in $a; do python check_exposure_pixel_file.py $i;done | tee check_exposure_pixel_LOT_FUOri.log


