#!/usr/bin/python3.4

# Project Euler:
# Problem #7: 10001st Prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10001st prime?
#
# Answer: 104743

import math
import sys

def find_prime(nth):
    primes = [2,3]
    n = len(primes)
    #print("Starting primes:",primes)
    test = primes[-1]
    while n <= nth:
        #print("Last prime:",primes[-1])
        test = test + 2
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
                n = n + 1
                break
    #print(primes)
    return primes[nth - 1]


def main():
    if len(sys.argv) > 1:
        nthprime = int(sys.argv[1])
    else:
        nthprime = 6

    prime = find_prime(nthprime)
    print("nth prime, n =",nthprime,":",prime)

main()
