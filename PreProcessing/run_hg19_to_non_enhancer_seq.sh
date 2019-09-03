#!/bin/bash

dataDir=$1
seqDir=$2

cd $dataDir
for file in *.txt; do

	if [[ "$file" == *"nonenhancers"* ]]; then
		cp $file $seqDir
	fi
done

cd $seqDir
for file in *.txt; do
	cellLine=$file | cut -d '_' -f1
	cat $cellLine".nenseq"
	while read -r line
	do
		chr=$line | cut -d ' ' -f1 
		start=$line | cut -d ' ' -f2 
		end=$line | cut -d ' ' -f3
		./twoBitToFa hg19.2bit stdout -seq=$chr -start=$start -end=$end

		echo $chr $start $end $seq >> $file".nenseq"
	done < $file
done