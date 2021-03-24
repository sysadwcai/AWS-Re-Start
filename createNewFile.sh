#! /bin/bash
# auto-create file with seq command

PREFIX=file
echo -e 'Please provide COUNT value:\c'
read -r COUNT1

FILENUM=$(ls | grep '$PREFIX.[0-9]*' | wc -l)

str=$(($FILENUM+1))
end=$(($str+$COUNT1-1))

if (($FILENUM > 0)); then
    for i in $(seq $str $end);
    do
        touch $PREFIX.$i
    done
else
    for i in `seq $COUNT1`
    do
        touch $PREFIX.$i
    done
fi
    
