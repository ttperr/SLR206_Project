#!/bin/bash

dir=.
output_dir=${dir}/output

threads="1 4 6 8 10 12"
list_sizes="100 1000 10000"
uratio="0 10 100" # update ratios
duration="2000"
warmup="0"

filename=data.csv

if [ ! -d "${output_dir}" ]; then
  mkdir $output_dir
fi
if [ ! -d "${output_dir}/data" ]; then
  mkdir ${output_dir}/data
fi

benchs="linkedlists.lockbased.CoarseGrainedListBasedSet linkedlists.lockbased.HandOverHandListBasedSet linkedlists.lockbased.LazyLinkedListSortedSet"
for bench in ${benchs}; do
  touch ${output_dir}/data/${bench:22}_${filename}
  echo "throughput,threads,uratio,lsize" > ${output_dir}/data/${bench:22}_${filename}
  for uratio in ${uratio}; do
    for t in ${threads}; do
       for i in ${list_sizes}; do
         grep Throughput ${dir}/${output_dir}/log/${bench}-i${i}-u${uratio}-t${t}-w${warmup}-d${duration}.log | awk -v ORS="," '{print $3}' >> ${output_dir}/data/${bench:22}_${filename}
         echo -n ${t} >> ${output_dir}/data/${bench:22}_${filename}
         echo -n ',' >> ${output_dir}/data/${bench:22}_${filename}
         echo -n ${uratio} >> ${output_dir}/data/${bench:22}_${filename}
         echo -n ',' >> ${output_dir}/data/${bench:22}_${filename}
         echo ${i} >> ${output_dir}/data/${bench:22}_${filename}
       done
    done
  done
done
