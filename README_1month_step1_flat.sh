#a='202104'
a=$1

#list_dark_time='005S 010S 030S'


for i in $a;do

  echo "generate master flat [B 30sec, V 10sec, R 5sec]"
  echo "python slt_calibration_master_1month_flat.py $i| tee 'slt_calibration_master_1month_flat_'$i'.log' "
  python slt_calibration_master_1month_flat.py $i

done



