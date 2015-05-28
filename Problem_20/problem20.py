#!/usr/bin/python3.4

# Project Euler:
# Problem #20: Factorial Digit Sum
#
# n! means n x (n - 1) x ... x 3 x 2 x 1
#
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 362880
# and the sum of the digits in the number 10! =
# 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
#
# Find the sum of the digits in the number 100!
#
# Answer: 648

import sys
import math

def digit_sum(n):
    print("start")
    number = n
    nsum = 0
    while number > 0:
        dig = number % 10
        print(dig)
        number = number // 10
        nsum += dig
    return nsum

def main():
    if len(sys.argv) > 1:
        fact_num = int(sys.argv[1])
    else:
        fact_num = 10
    factorial = math.factorial(fact_num)
    fdsum = digit_sum(factorial)
    print("Sum of", str(fact_num) + "! =",factorial,"digits:",fdsum)

if __name__ == '__main__':
    main()
