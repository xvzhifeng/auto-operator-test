cd `dirname $1`

result=''

function ReadAllFileName()
{
  if [ "X$1" != 'X' ]
   then
         cd "$1"
  fi

  files=`ls`
for filename in $files;do

	if [ -d $filename ]
    	then
		#echo  "文件夹 $filename "
	        #递归
		ReadAllFileName $filename

	else

	if [ ${filename##*.} = 'cpp' ] || [ ${filename##*.} = 'c' ]
	 then
		#	echo $filename
		  result=${result}" "$filename
	fi

	fi
done
	cd ..
}

ReadAllFileName


echo $result