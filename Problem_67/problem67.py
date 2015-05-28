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
# Find the maximum total from top to bottom in triangle.txt (right click and
# 'Save Link/Target As...'), a 15k text file containing a triangle with one-
# hundred rows.
#
# NOTE: This is a much more difficult version of <Problem 18>. It is not
# possible to try every route to solve this problem, as there are 2^99
# altogether! If you could check on trillion (10^12) routes every second it
# would take over twenty billion years to check them all. There is an
# efficient algorithm to solve it. ;o)
#
# Answer: 7273

import sys

def find_max_path_sum(fn):
    with open(fn) as f:
        pyr = [[int(x) for x in line.split()] for line in f]
    #print(pyr)
    for i in range(1,len(pyr))[::-1]:
        for j in range(0,len(pyr[i])-1):
            #print("Then pyr[i-1][j] =",pyr[i-1][j])
            pyr[i-1][j] = max(pyr[i][j]+pyr[i-1][j],pyr[i][j+1] + pyr[i-1][j])
            #print("Now pyr[i-1][j] =",pyr[i-1][j])
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
