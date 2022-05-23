"""
======================
# -*-coding: utf8-*-
# @Author  : louiss007
# @Time    : 22-5-23 下午10:52
# @FileName: filter_null_sample.py
# @Email   : quant_master2000@163.com
======================
"""

import json
import os


def shell_cmd(cmd):
    os.system(cmd)


def filter_null_sample(in_path):
    dirs = os.listdir(in_path)

    for dir in dirs:
        if dir.find('json') != -1 or dir.find('md') != -1:
            continue
        train_file = '{ip}/{dir}/train.json'.format(ip=in_path, dir=dir)
        train_file_bak = '{ip}/{dir}/train.json.bak'.format(ip=in_path, dir=dir)
        new_train_file_filter = '{ip}/{dir}/train_filter.json'.format(ip=in_path, dir=dir)
        new_train_file = '{ip}/{dir}/train.json'.format(ip=in_path, dir=dir)
        print(new_train_file_filter)
        fo = open(new_train_file_filter, 'w')
        tot_cnt = 0
        filter_tot_cnt = 0
        with open(train_file, 'r') as fi:
            for line in fi.readlines():
                tot_cnt += 1
                data_map = json.loads(line.strip())
                entity = data_map.get('entity')
                relation = data_map.get('relation')
                event = data_map.get('event')
                if len(entity) == 0 and len(relation) == 0 and len(event) == 0:
                    continue
                filter_tot_cnt += 1
                fo.write(line)
            print("%s: %f" % (dir, filter_tot_cnt * 1.0/tot_cnt))
        cmd1 = 'mv {sf} {tf}'.format(sf=train_file, tf=train_file_bak)
        cmd2 = 'mv {sf} {tf}'.format(sf=new_train_file_filter, tf=new_train_file)
        shell_cmd(cmd1)
        shell_cmd(cmd2)
        fo.close()


if __name__ == '__main__':
    proj_path = os.path.dirname(__file__).rsplit('/', 1)[0]
    data_path = '{pp}/data/duuie'.format(pp=proj_path)
    filter_null_sample(data_path)
