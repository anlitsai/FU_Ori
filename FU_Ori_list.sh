b='202010 202011 202012 202101 202102 202103 202104'; 

cd ../
echo `pwd`

for i in $b;do echo $i;find gasp/$i |grep FU_Ori-$i[0-3][0-9] |cut -d / -f1-3|cut -d _ -f1 |sort|uniq; done

cd FU_Ori
echo `pwd`
