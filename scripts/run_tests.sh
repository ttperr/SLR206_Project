#!/bin/bash

dir=.
output_dir=${dir}/output
bin=${bin}/bin
java=java

threads="1 4 6 8 10 12"
list_sizes="100 1000 10000"
uratios="0 10 100" # update ratios
duration="2000"
warmup="0"

CP=bin
MAINCLASS=contention.benchmark.Test

if [ ! -d "${output_dir}" ]; then
  mkdir $output_dir
fi
if [ ! -d "${output_dir}/log" ]; then
  mkdir ${output_dir}/log
fi

benchs="linkedlists.lockbased.CoarseGrainedListBasedSet linkedlists.lockbased.HandOverHandListBasedSet linkedlists.lockbased.LazyLinkedListSortedSet"

for bench in ${benchs}; do
  for uratio in ${uratios}; do
    for t in ${threads}; do
       for i in ${list_sizes}; do
         r=$((2*${i})) #list range twice as big as the list size
         out=${output_dir}/log/${bench}-i${i}-u${uratio}-t${t}-w${warmup}-d${duration}.log
         echo "${java} -cp ${CP} ${MAINCLASS} -W ${warmup} -u ${uratio} -d ${duration} -t ${t} -i ${i} -r ${r} -b ${bench}"
         ${java} -cp ${CP} ${MAINCLASS} -W ${warmup} -u ${uratio} -d ${duration} -t ${t} -i ${i} -r ${r} -b ${bench} 2>&1 > ${out}
       done
    done
  done
done
