#!/usr/bin/python3.4

# Project Euler:
# Problem #13: Large Sum
#
# Work out the first ten digist of the sum of the following one-hundred
# 50-digit numbers.
#
# <numbers in file 'long_numbers'>
#
# Answer: 5537376230

import math
import sys

def find_digit_sum(fn,dig):
    total_sum = 0
    f = open(fn,'r')
    for number in f:
        total_sum += int(number)
    f.close()
    digits = int(math.log10(total_sum)) + 1
    mods = 10 ** (digits - dig)
    if total_sum % 10 == 0:
        digs = total_sum  // mods
    else:
        digs = (total_sum - (total_sum % mods))//mods
    return digs

def main():
    if len(sys.argv) > 2:
        num_file = sys.argv[1]
        digits = int(sys.argv[2])
    else:
        num_file = "long_numbers"
        digits = 10
    sum_digits = find_digit_sum(num_file,digits)
    print("First",digits,"digits of sum:",sum_digits)

if __name__ == '__main__':
    main()
