#a='202003'
a=$1

list_dark_time='005S 010S 030S'


for i in $a;do
  echo "generate master bias"
  echo "python slt_calibration_master_1month_bias.py $a| tee 'slt_calibration_master_1month_bias_'$i'.log' "
  python slt_calibration_master_1month_bias.py $a

done



