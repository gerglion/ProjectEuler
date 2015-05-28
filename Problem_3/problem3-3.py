#!/usr/bin/python3.4

# Project Euler:
# Problem #3: Largest Prime Factor
# The prime factors of 13195 are 5,7,13, and 29.
#
# What is the largest prime factor of the number 600851475143
#
# Answer: 6857
import math
import sys

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

def main():
    if len(sys.argv) > 1:
        magic_number = int(sys.argv[1])
    else:
        #magic_number = 13195
        magic_number = 600851475143
    print("Magic number: ",magic_number)
    print("Prime barrier: ",int(math.sqrt(magic_number)))
    prime_factors = factor(magic_number)
    top_prime_factor = 1
    print("Factors:")
    for i in prime_factors:
        print(i,"^",prime_factors[i])
        if i > top_prime_factor:
            top_prime_factor = i
    print("Top prime factor:",top_prime_factor)

main()
