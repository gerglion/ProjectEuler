#!/usr/bin/python3.4

# Project Euler:
# Problem #21: Amicable Numbers
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than
# n which divide evenly into n).
#
# If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55, and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2,
# 4, 71, and 142; so d(284) = 220.
#
# Evaluate the sum of all amicable numbers under 10000.
#
# Answer: 31626

import sys
import math

def find_divisors(n):
    lim = math.ceil(math.sqrt(n))
    divisors = [1]
    for i in range(2,lim):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)
    return divisors

def sum_amicable_numbers(bnd):
    amic_list = []
    for i in range(1,bnd):
        t1 = sum(find_divisors(i))
        t2 = sum(find_divisors(t1))
        if i != t1 and t2 == i:
            print("Amicable:",i,",",t1)
            amic_list.append(i)
            amic_list.append(t1)

    else:
        amic_list = sorted(set(amic_list))
        print(amic_list)
    return sum(amic_list)

def main():
    if len(sys.argv) > 1:
        bound = int(sys.argv[1])
    else:
        bound = 20
    amic_sum = sum_amicable_numbers(bound)
    print("Sum of amicable numbers under",bound,":",amic_sum)

if __name__ == '__main__':
    main()
