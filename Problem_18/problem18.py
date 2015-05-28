#!/usr/bin/python3.4

# Project Euler:
# Problem #18: Maximum Path Sum I
#
# By starting at the top of the triangle below and moving to the adjacent
# numbers on the row below, the maximum total from top to bottom is 23.
#
#    3
#   7 4
#  2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
# <number triangle in file 'number_pyramid'>
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem
# by trying every routes. However, <Problem 67>, is the same challenge with a
# triangle containing one-hundred rows; it cannot be solved by brute force,
# and requires a clever method! ;o)
#
# Answer: 1074

import sys

def find_max_path_sum(fn):
    with open(fn) as f:
        pyr = [[int(x) for x in line.split()] for line in f]
    for i in range(1,len(pyr))[::-1]:
        for j in range(0,len(pyr[i])-1):
            #pyr[i-1][j] = max(pyr[i][j]+pyr[i-1][j],pyr[i][j+1] + pyr[i-1][j])
            pyr[i-1][j] += max(pyr[i][j],pyr[i][j+1])
    return pyr[0][0]


def main():
    if len(sys.argv) > 1:
        pyr_file = sys.argv[1]
    else:
        pyr_file = 'pyramid_test'
    max_path_sum = find_max_path_sum(pyr_file)
    print("Maximum path sum:",max_path_sum)

if __name__ == '__main__':
    main()
