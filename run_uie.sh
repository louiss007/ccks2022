#!/usr/bin/env bash

cur_path=$(dirname `readlink -f $0`)
echo $cur_path

# get train data
python task1/baseline/process_data.py preprocess

## train model
#cd task1/baseline
#sh run_train.sh
#cd..
#cd..
# get test data
python task1/baseline/process_data.py split-test

# inference
model=output/task1/duuie_multi_task_b8_lr5e-4
python task1/baseline/inference.py --data output/task1/duuie_test_a --model ${model}

# merge test-pred for submit result
python task1/baseline/process_data.py merge-test
