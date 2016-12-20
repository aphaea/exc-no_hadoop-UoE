#!/usr/bin/python

# Implementation of Bloom filter, The probability that a line (and its
# duplicates) from the input does not appear at all in the output is less than 1%

# Use: python bloomF.py <num_of_lines in file>  < webLarge.txt > outfile.txt


import math
import sys
#from bitarray import bitarray ###Uncomment this line if bitarray is installed

def BloomFInit(num_lines, false_pos):

        filter_size = int(math.ceil(-(num_lines*math.log(false_pos)/float(math.log(2)**2))))
        num_hf = int(math.ceil((filter_size/float(num_lines))*math.log(2)))
        bloom_f = [0]*filter_size
        # Replace the above line with following 2 lines if bittaray is installed
        #bloom_f = bitarray(filter_size)
        #bloom_f.setall(0)
        return bloom_f, num_hf, filter_size

def AddLine(line, num_hashes, bloom_filter, filter_size):

        for seed in range(1, num_hashes+1):
                seed_line = str(seed) + '_' + line
                hashing = hash(seed_line)
                hashing = hashing % filter_size
                bloom_filter[hashing] = 1
        return bloom_filter

def LookUpLine(num_hashes, line, bloom_filter, filter_size):

        exist = 1
        for seed in range(1, num_hashes+1):
                seed_line = str(seed) + '_' + line
                hashing = hash(seed_line)
                hashing = hashing % filter_size
                if bloom_filter[hashing] == 0:
                        exist = 0
                        break
                else:
                        continue
        return exist

if __name__ == "__main__":
        num_lines = int(sys.argv[1])
        false_pos = 0.01
        bloom_filter, num_hashes, filter_size = BloomFInit(num_lines, false_pos)
        
        counter = 0
        for line in sys.stdin:
                counter += 1
                if counter <= num_lines:
                        line = line.strip()
                        check_line = line
                        exist = LookUpLine(num_hashes, check_line, bloom_filter,filter_size)
                        if exist == 0:
                                bloom_filter = AddLine(check_line, num_hashes, bloom_filter, filter_size)
                                print(line)
                else:
                        break

