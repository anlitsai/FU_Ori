b='202010 202011 202012 202101 202102 202103 202104'; 

cd ../
echo `pwd`

for i in $b;do c=`find gasp/$i |grep FU_Ori-$i[0-3][0-9] |cut -d / -f1-3|cut -d _ -f1 |sort|uniq`; echo "rsync -av $c FU_Ori/$i/" ; rsync -av $c FU_Ori/$i/; done


cd FU_Ori
echo `pwd`

