#!/usr/bin/env bash

export CUDNN_HOME=/home/louiss007/Downloads/cuda_software/cuda
export LD_LIBRARY_PATH=$CUDNN_HOME/lib64:$LD_LIBRARY_PATH
export CPLUS_INCLUDE_PATH=$CUDNN_HOME/include:$CPLUS_INCLUDE_PATH

python run_seq2struct.py                              \
  --multi_task                                         \
  --multi_task_config config/multi-task-duuie.yaml     \
  --negative_keep 1.0                                  \
  --do_train                                           \
  --metric_for_best_model=all-task-ave                 \
  --model_name_or_path=./uie-char-small                \
  --max_source_length=192                              \
  --max_prefix_length=-1                               \
  --max_target_length=192                              \
  --num_train_epochs=10                                \
  --train_file=../../output/task1/duuie/train.json               \
  --validation_file=../../output/task1/duuie/val.json            \
  --record_schema=../../output/task1/duuie/record.schema         \
  --per_device_train_batch_size=8                     \
  --per_device_eval_batch_size=256                     \
  --output_dir=../../output/task1/duuie_multi_task_b32_lr5e-4      \
  --logging_dir=../../output/task1/duuie_multi_task_b32_lr5e-4_log \
  --learning_rate=5e-4                                 \
  --seed=42                                            \
  --overwrite_output_dir                               \
  --gradient_accumulation_steps 2
