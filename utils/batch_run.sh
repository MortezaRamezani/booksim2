#!/bin/sh

#sed -i "s/\(k *= *\).*/\18;/" torus_16.run

#.\src\booksim.exe .\runfiles\torus_16x16  "k=4"
#.\src\booksim.exe .\runfiles\torus_16x16  "k=8"
#.\src\booksim.exe .\runfiles\torus_16x16  "k=16"


#declare -a k_size=("4" "8" "16")
declare -a k_size=("4")
declare -a traffic_pattern=("bitcomp" "bitrev" "butterfly" "shuffle" "neighbor" "uniform" "transpose" "tornado")
#declare -a traffic_pattern=("bitcomp")
declare -a load_rate=("0.02" "0.04" "0.06" "0.08" "0.1" "0.12" "0.14" "0.16" "0.18" "0.2")
declare -a num_of_vc=("2" "4")

dir="./results/"$(date +"%Y%m%d_%H%M")
mkdir -p $dir

for k in "${k_size[@]}"
do
	for t in "${traffic_pattern[@]}"
	do
		for nv in "${num_of_vc[@]}"
		do
		  for ld in $(seq 0.01 0.01 0.5)
			do 
			   run_date=$(date +"%Y-%m-%d_%H%M")
			   ./src/booksim ./runfiles/general_run "k=$k" "traffic=$t" "num_vcs=$nv" "injection_rate=$ld"\
			   "stats_out=$dir/stats_"$k"x"$k"_"$t"_"$nv"VC_"$ld"_"$run_date"" > $dir/out_"$k"x"$k"_"$t"_"$nv"VC_"$ld"_"$run_date" &
			done
		done
	done
done