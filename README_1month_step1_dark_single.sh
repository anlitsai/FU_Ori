#a='202103'
a=$1

#list_dark_time='005S 010S 030S'
#dark_time='005S'
#dark_time='010S'
#dark_time='030S'
dark_time=$2

echo "generate master dark $dark_time"
echo "python slt_calibration_master_1month_dark_single.py $a $dark_time | tee 'slt_calibration_master_1month_dark_single_'$a'_'$dark_time'.log' "
python slt_calibration_master_1month_dark_single.py $a $dark_time


