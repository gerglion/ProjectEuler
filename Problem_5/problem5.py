#!/usr/bin/python3.4

# Project Euler:
# Problem #5: Smallest Multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# Answer: 232792560

import math
import sys
import timeit

def factor(num):
    factors = {}
    n = num
    for i in range(2,int(math.sqrt(num))+1):
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n = n // i
    if n > 1:
        factors[n] = 1
    return factors

def all_factorization(lo,up):
    all_factors = {}

    for i in range(lo,up + 1):
        factors = factor(i)
        for fact in factors:
            if fact in all_factors:
                if factors[fact] > all_factors[fact]:
                    all_factors[fact] = factors[fact]
            else:
                all_factors[fact] = factors[fact]

    return all_factors
def run_main():
    if len(sys.argv) > 2:
        lower = int(sys.argv[1])
        upper = int(sys.argv[2])

    else:
        lower = 1
        upper = 8

    all_f = all_factorization(lower,upper)
    product = 1
    for f in all_f:
        #print("Product:",product,"*",f,"^",all_f[f])
        product = product * (f ** all_f[f])
    print("Total product:",product)

def main():
    print(timeit.timeit("run_main()",setup="from __main__ import test",number=1000))

main()
