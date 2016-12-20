#!/usr/bin/python

# Lossy counting on queries, output contains all queries that form at least 1% of all queries 
# and no query that formed less than 0.9% of all queries

# Use: python lossy_count.py  < queriesLarge.txt > outfile.txt

import sys
import math

b_cur = 1
count = 0
dict_q = {}
epsilon = 0.1/100
w = math.ceil(1./epsilon)

def removekey(dict_A, key):
    dict_A_cp = dict(dict_A)
    del dict_A_cp[key]
    return dict_A_cp

for line in sys.stdin:
        line = line.strip()
        count += 1
        if line in dict_q:
                q_list = dict_q.get(line)
                q_list[0] += 1
                dict_q[line] = q_list
        else:
                q_list = []
                q_list.append(1)
                q_list.append(b_cur-1)
                dict_q.update([(line, q_list)])

        if count%w == 0:

                for line, values in dict_q.items():
                        freq = values[0]
                        delta = values[1]
                        if (freq+delta <= b_cur):
                                dict_q = removekey(dict_q, line)
                b_cur += 1

for line, values in dict_q.items():
        freq = values[0]
        if (freq >= (0.9/100)*count):
                print(line)
