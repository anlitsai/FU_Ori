
#d1='20201001'
#d2='20210430'
#echo "$d1 -- $d2"

#filter='V B R'
#fi='V'
#fi='B'
#fi='R'

#python slt_InstMag_Vmag_aperture_annulus_r_file_median_w1_subplot_date_FU_Ori.py $d1 $d2 | tee 'slt_InstMag_Vmag_aperture_annulus_r_file_median_w1_subplot_'$d1'-'$d2'_V.log'
#python slt_InstMag_Bmag_aperture_annulus_r_file_median_w1_subplot_date_FU_Ori.py $d1 $d2 | tee 'slt_InstMag_Bmag_aperture_annulus_r_file_median_w1_subplot_'$d1'-'$d2'_B.log'
#python slt_InstMag_Rmag_aperture_annulus_r_file_median_w1_subplot_date_FU_Ori.py $d1 $d2 | tee 'slt_InstMag_Rmag_aperture_annulus_r_file_median_w1_subplot_'$d1'-'$d2'_R.log'

skip_refstar_V='C'

#python slt_InstMag_Vmag_aperture_annulus_r_file_median_w1_subplot_date_FU_Ori.py $skip_refstar_V | tee 'slt_InstMag_Vmag_aperture_annulus_r_file_median_w1_subplot_V_skip'+$skip_refstar_V+'.log'
python slt_InstMag_Vmag_aperture_annulus_r_file_median_w1_subplot_date_FU_Ori.py | tee 'slt_InstMag_Vmag_aperture_annulus_r_file_median_w1_subplot_V.log'
python slt_InstMag_Bmag_aperture_annulus_r_file_median_w1_subplot_date_FU_Ori.py | tee 'slt_InstMag_Bmag_aperture_annulus_r_file_median_w1_subplot_B.log'
python slt_InstMag_Rmag_aperture_annulus_r_file_median_w1_subplot_date_FU_Ori.py | tee 'slt_InstMag_Rmag_aperture_annulus_r_file_median_w1_subplot_R.log'

