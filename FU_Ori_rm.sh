a=`find ./|grep GASP|cut -d / -f1-5|sort|uniq`

rm -rf $a
