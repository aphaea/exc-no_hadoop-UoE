#!/usr/bin/python


# Reservoir sampling of  multiple lines uniformly without replacement
# running on a single machine

#Use: python random_fun.py < webLarge.txt > outfile.txt

import sys
import random

random.seed(10)
reservoir_l = []
line_num = 0

for line in sys.stdin:
        if line_num < 100:
                reservoir_l.append(line.strip())
        else:
                prob = random.randint(0,line_num)
                if prob < 100:
                        reservoir_l[prob] = line.strip()
        line_num += 1

for l in reservoir_l:
        print(l)
