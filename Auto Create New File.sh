#! /bin/bash
# auto-create file with seq command

PREFIX=file
echo -e 'Please provide COUNT value: \c'
read -r COUNT1

filenum=$(ls | grep "file.[0-9]*" | wc -l)

str=$(($filenum+1))
end=$(($str+$COUNT1-1))
echo $end
if (($filenum > 0)); then

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
