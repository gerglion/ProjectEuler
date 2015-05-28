#!/usr/bin/python3.4

# Project Euler:
# Problem #24: 1000-digit Fibonacci Number
#
# The Fibonacci sequence is defined by the recurrence relation:
#   F_n = F_n-1 + F_n-2, where F_1 = 1 and F_2 = 1.
#
# Hence, the first 12 terms will be:
#   F_1 = 1
#   F_2 = 1
#   F_3 = 2
#   F_4 = 3
#   F_5 = 5
#   F_6 = 8
#   F_7 = 13
#   F_8 = 21
#   F_9 = 34
#   F_10 = 55
#   F_11 = 89
#   F_11 = 144
#
# The 12th term, F_12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain
# 1000 digits?
#
# Answer: 4782

import sys
import math

def find_fib_of_dig(d):
    pprev = 1
    prev = 1
    cur = prev + pprev
    count = 3
    while(int(math.log10(cur))+1 < d):
        #print(count,cur)
        pprev = prev
        prev = cur
        cur = prev + pprev
        count += 1
    #print(count,cur)
    return count

def main():
    ARG_LEN = len(sys.argv)
    if ARG_LEN > 1:
        dig = int(sys.argv[1])
    else:
        dig = 3

    first_dig = find_fib_of_dig(dig)
    print("First Fibonacci number with",dig,"digits: #",first_dig)
if __name__ == '__main__':
    main()
