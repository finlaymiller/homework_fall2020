#!/bin/bash
set -eux
mkdir -p data

for env in Ant HalfCheetah Hopper Humanoid Walker2d
do
	python cs285/scripts/run_hw1.py --expert_policy_file cs285/policies/experts/$env.pkl --env_name $env-v2 --exp_name dagger_$env --n_iter 10 --do_dagger --expert_data cs285/expert_data/expert_data_$env-v2.pkl --video_log_freq -1
done

python a.py
