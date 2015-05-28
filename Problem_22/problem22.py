#!/usr/bin/python3.4

# Project Euler:
# Problem #22: Name Scores
#
# Using <names.txt>, a 46k text file containing over five-thousand first
# names, begin by sorting it into alphabetical order. Then working out the
# alphabetical value for each name, multiply this value by its alphabetical
# position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which
# is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
# COLIN would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?
#
# Answer: 871198282

import sys

def name_score(name):
    score = 0
    for c in name:
        score += (ord(c)-64)
    return score


def score_names(nf):
    names_list = []
    with open(nf,'r') as f:
        read = f.read()
        nstr = read.strip('"')
        for name in nstr.split('","'):
            names_list.append(name)
    f.close()
    names_list.sort()
    ns_sum = 0
    for n in range(0,len(names_list)):
        score = name_score(names_list[n])
        ns = n + 1
        tscore = score * ns
        #print(names_list[n],":",score,"*",ns,"=",tscore)
        ns_sum += tscore
    return ns_sum

def main():
    if len(sys.argv) > 1:
        name_file = sys.argv[1]
    else:
        name_file = "names.txt"

    name_score_sum = score_names(name_file)
    print("Total name score sum:",name_score_sum)

if __name__ == '__main__':
    main()
