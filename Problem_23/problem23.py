#!/usr/bin/python3.4

# Project Euler:
# Problem #23: Non-Abundant Sums
#
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
# number.
#
# A number n is called deficient if the sum of its proper divisors is less
# than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number,  1 + 2 + 3 + 4 + 6 = 16, the
# smallest number that can be written as the sum of two abundant numbers is
# 24. By mathematical analysis, it can be shown that all integers greater
# than 28123 can be written as the sum of two abundant numbers. However, this
# upper limit cannot be reduced any further by analysis even though it is
# known that the greatest number that cannot be expressed as the sum of two
# abundant numbers is less than this limit.
#
# Find the sum of all positive integers which cannot be written as the sum of
# two abundant numbers.
#
# Answer: 4179871

import sys
import math

def find_divisors(n):
    lim = math.ceil(math.sqrt(n))
    divisors = set()
    for i in range(2,lim + 1):
        if n != i and n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    divisors.add(1)
    return divisors

def perfect_number(n):
    div = find_divisors(n)
    #print(n,":",div)
    sdiv = sum(div)
    ndiv = sdiv - n
    return ndiv

def find_abundant_num(lim):
    a_num = []
    for i in range(1,lim+1):
        if perfect_number(i) > 0:
            a_num.append(i)
    return a_num

def find_non_abun_sum_sum(lim):
    a_numbers = set(find_abundant_num(lim))
    ansl = sorted(list(a_numbers))
    nset = set()
    for i in ansl:
        for j in ansl:
            tmp = i + j
#            nset.add(tmp)
            if tmp > lim:
                break
            else:
                nset.add(tmp)
    aset = {x for x in range(1,lim+1)}
    ans = aset - nset
    return sum(ans)

def main():
    if len(sys.argv) > 1:
        limit = int(sys.argv[1])
    else:
        limit = 28123

    total_sum = find_non_abun_sum_sum(limit)
    print("Sum:",total_sum)

if __name__ == '__main__':
    main()
