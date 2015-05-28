#!/usr/bin/python3.4

# Project Euler:
# Problem #9: Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#  a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triple for which a + b + c = 1000.
# Find the product abc
#
# Answer: 31875000

import math
import sys

def find_pythagorean_triplets(sum):
    for a in range(1,sum//3):
        for b in range(a+1,sum//2):
            for c in range(b+1,sum):
                if a + b + c == 1000:
                    if a ** 2 + b ** 2 == c ** 2:
                        print("PT:",a,b,c)
                        return a * b * c
def main():
    if len(sys.argv) > 1:
        pt_sum = int(sys.argv[1])
    else:
        pt_sum = 1000

    product = find_pythagorean_triplets(pt_sum)
    print("Pythagorean triplet (sum = 1000) product:",product)

main()
