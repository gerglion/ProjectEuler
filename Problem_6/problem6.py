#!/usr/bin/python3.4

# Project Euler:
# Problem #6: Sum Square Difference
#
# The sum of the squares of the first ten natural numbers is,
#       1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
#        (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference bewteen the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#
# Answer: 25164150

import math
import sys

def main():
    if len(sys.argv) > 1:
        natural = int(sys.argv[1])
    else:
        natural = 10

    sq_sum = natural * ( natural + 1 ) // 2
    sum_sq = ( 2 * natural + 1 ) * ( natural + 1 ) * natural // 6
    diff = sq_sum ** 2 - sum_sq
    print(sq_sum ** 2,"-",sum_sq,"=",diff)
main()
