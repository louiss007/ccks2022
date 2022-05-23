#!/usr/bin/env bash


cur_path=$(cd $(dirname $0); pwd)
echo ${cur_path}

export CUDNN_HOME=/home/louiss007/Downloads/cuda_software/cuda
export LD_LIBRARY_PATH=$CUDNN_HOME/lib64:$LD_LIBRARY_PATH
export CPLUS_INCLUDE_PATH=$CUDNN_HOME/include:$CPLUS_INCLUDE_PATH

python3 ${cur_path}/inference.py --data data/duuie_test_a --model output/duuie_multi_task_b16_lr3e-4