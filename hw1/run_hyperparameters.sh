#!/bin/bash
set -eux
mkdir -p data

# for steps in 1 100 1000 10000 100000
# for size in 16 32 64 128 256
for n in 1 2 3 4 5
do
	python cs285/scripts/run_hw1.py --expert_policy_file cs285/policies/experts/Humanoid.pkl --env_name Humanoid-v2 --exp_name bc_Humanoid --n_iter 1 --expert_data cs285/expert_data/expert_data_Humanoid-v2.pkl --video_log_freq -1 --n_layers $n
done

python make_graphs.py -v n_layers