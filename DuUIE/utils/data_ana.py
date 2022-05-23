"""
======================
# -*-coding: utf8-*-
# @Author  : louiss007
# @Time    : 22-5-23 下午10:51
# @FileName: data_ana.py
# @Email   : quant_master2000@163.com
======================
"""

import json
import sys


def data_ana(in_file, out_file):
    sample_cnt = 0
    null_sample_cnt = 0
    entity_label2nums = {}
    relation_label2nums = {}
    event_label2nums = {}
    fi = open(in_file, 'r')
    for line in fi.readlines():
        data_map = json.loads(line.strip())
        sample_cnt += 1
        entity = data_map.get('entity')
        if len(entity) == 0:
            null_sample_cnt += 1
        relation = data_map.get('relation')
        # if len(relation) == 0:
        #     null_sample_cnt += 1

        # event = data_map.get('event')
        # if len(event) == 0:
        #     null_sample_cnt += 1
        # print(event)
        # sys.exit(1)
        # for item in entity:
        #     label = item.get('text')
        #     entity_label2nums.setdefault(label, 0)
        #     entity_label2nums[label] += 1

    print(sample_cnt)
    print(null_sample_cnt)
    print(null_sample_cnt*1.0/sample_cnt)
    # fi.close()
    # fo = open(out_file, 'w')
    # for kv in sorted(entity_label2nums.items(), key=lambda x: x[1], reverse=True):
    #     data = '\t'.join([kv[0], str(kv[1])])
    #     print(data)
    #     fo.write(data+'\n')
    # fo.write('sample cnt: %d\n' % sample_cnt)
    # fo.close()


if __name__ == '__main__':
    # in_file = '../data/duuie/CONV-ASA/train.json'
    # in_file = '../data/duuie/DUEE/train.json'
    # in_file = '../data/duuie/DUEE_FIN_LITE/train.json'
    # in_file = '../data/duuie/DUIE_LIFE_SPO/train.json'
    # in_file = '../data/duuie/DUIE_ORG_SPO/train.json'
    # in_file = '../data/duuie/MSRA/train.json'
    in_file = '../data/duuie/PEOPLE_DAILY/train.json'
    #
    # out_file = '../output/duuie/CONV-ASA/train_entity_ana.txt'
    # out_file = '../output/duuie/DUEE/train_entity_ana.txt'
    # out_file = '../output/duuie/DUEE_FIN_LITE/train_entity_ana.txt'
    # out_file = '../output/duuie/DUIE_LIFE_SPO/train_entity_ana.txt'
    # out_file = '../output/duuie/DUIE_ORG_SPO/train_entity_ana.txt'
    # out_file = '../output/duuie/MSRA/train_entity_ana.txt'
    # out_file = '../output/duuie/PEOPLE_DAILY/train_entity_ana.txt'
    #
    # out_file = '../output/duuie/CONV-ASA/train_relation_ana.txt'
    # out_file = '../output/duuie/DUEE/train_relation_ana.txt'
    # out_file = '../output/duuie/DUEE_FIN_LITE/train_relation_ana.txt'
    # out_file = '../output/duuie/DUIE_LIFE_SPO/train_relation_ana.txt'
    # out_file = '../output/duuie/DUIE_ORG_SPO/train_relation_ana.txt'
    # out_file = '../output/duuie/MSRA/train_relation_ana.txt'
    out_file = '../output/duuie/PEOPLE_DAILY/train_relation_ana.txt'

    data_ana(in_file, out_file)
