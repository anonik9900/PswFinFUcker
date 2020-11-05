#python pswf.py tempfile.txt
#var=`cat tempfile.txt` 
#rm tempfile.txt


#!/bin/sh 

#num=2 
#text=`python test.py $num` 
#echo "$num as text is $text" 
#value=`python test.py $pas_val `

var=`python test.py`

echo 


crunch 4 4 $var
