#!/usr/bin/python3.4

# Project Euler:
# Problem #10: Summation of Primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
#
# Find the sum of all the primes below two million.
#
# Answer: 142913828922

import math
import sys

def find_primes_below(bound):
    primes = [2,3]
    #print("Starting primes:",primes)
    test = primes[-1]+2
    while test <= bound:
        #print("Last prime:",primes[-1])
        #print("Test:",test)
        for i in primes:
            #print("i:",i)
            if i <= int(math.sqrt(test)):
                if test % i == 0:
                    #print("not prime")
                    break
            else:
                #print("prime")
                primes.append(test)
                break
        test = test + 2
    return primes

def main():
    if len(sys.argv) > 1:
        prime_sum_bound = int(sys.argv[1])
    else:
        prime_sum_bound = 10

    primes = find_primes_below(prime_sum_bound)
    #print("Primes below",prime_sum_bound,":",primes)
    print("Sum of primes:",(sum(primes)))

main()
