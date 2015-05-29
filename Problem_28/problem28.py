#!/usr/bin/python3.4

# Project Euler:
# Problem #28: Number Spiral Diagonals
#
# Starting with the number 1 and moving to the right in a clockwise direction
# a 5 by 5 spireal is formed as follows:
#       [21]  22  23  24  [25]
#        20  [ 7]  8 [ 9]  10
#        19    6 [ 1]  2   11
#        18  [ 5]  4 [ 3]  12
#       [17]  16  15  14  [13]
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way.
#
# Answer:

import sys

def sum_spi_sqr_diag(d):

    if d % 2 != 0:
        diag = 1
        last = 1
        for i in range(3,d+1,2):
            n = (i - 1) >> 1
            for j in range(4):
                num = last + 2 * n * (j+1)
                diag += num
            else:
                last = num
            #print(n,":",i,"x",i,":",diag)
        print("Diag sum:",diag)

def main():
    ARG_LEN = len(sys.argv)
    if ARG_LEN > 1:
        limit = int(sys.argv[1])
    else:
        limit = 9
    sum_spi_sqr_diag(limit)

if __name__ == '__main__':
    main()
