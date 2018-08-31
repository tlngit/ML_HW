#!/usr/bin/python
import sys

input_file = sys.argv[1]

with open(input_file, 'r') as f:
    all_words = f.read()
    words = all_words.strip().split(' ')
    word_list = []
    word_count = []

    for word in words:
        if word not in word_list:
            word_list = word_list + [word]
            word_count = word_count + [words.count(word)]

with open('Q1.txt','w') as out:
    ctr = 0
    for word in word_list:
        if ctr==(len(word_list)-1):
            out_str = word + ' ' + str(ctr) + ' ' + str(word_count[ctr])
        else:
            out_str = word + ' ' + str(ctr) + ' ' + str(word_count[ctr]) + '\n'
        #print(out_str)
        out.write(out_str)
        ctr = ctr + 1

