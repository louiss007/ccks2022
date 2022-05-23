#!/usr/bin/env bash

cur_path=$(cd $(dirname $0); pwd)
echo ${cur_path}
data_path=${cur_path}/data/
duuie_zip=${cur_path}/data/duuie.zip
duuie_test_a_zip=${cur_path}/data/duuie_test_a.zip
seen_schema_zip=${cur_path}/data/seen_schema.zip
if test -e ${duuie_zip}
then
	echo ${duuie_zip}
	#sh ${cur_path}/run_train.sh
else
	wget https://dataset-bj.cdn.bcebos.com/qianyan/duuie.zip -O ${duuie_zip}
	unzip ${duuie_zip} -d ${cur_path}/data
fi
if test -e ${duuie_test_a_zip}
then
	echo ${duuie_test_a_zip}
else
	wget https://dataset-bj.cdn.bcebos.com/qianyan/duuie_test_a.zip -O ${duuie_test_a_zip}
	unzip ${duuie_test_a_zip} -d ${cur_path}/data
fi
if test -e ${seen_schema_zip}
then
	echo ${seen_schema_zip}
else
	wget https://dataset-bj.cdn.bcebos.com/qianyan/seen_schema.zip -O ${seen_schema_zip}
	unzip ${seen_schema_zip} -d ${data_path}
fi
wait

train_path=${cur_path}/data/duuie_pre
if test -e ${train_path}
then
	sh ${cur_path}/run_train.sh
else
	python3 ${cur_path}/preprocess_data.py preprocess
fi