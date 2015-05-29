#!/usr/bin/python3.4

# Project Euler:
# Problem #27: Quadratic Primes
#
# Euler discovered the remarkable quadratic formula:
#
#   n^2 + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive
# values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1 ) + 41
# is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
# divisible by 41.
#
# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80
# primes for the consecutive values n = 0 to 79. The product of the
# coefficients, -79 and 1601, is -126479.
#
# Considering quadratics of the form:
#   n^2 + an + b, where |a| < 1000 and |b| < 1000
#
#   where |n| is the modulus/absolute value of n
#   e.g. |11| = 11 and |-4| = 4
#
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.
#
# Answer: -59231

import sys
import math

def is_prime(n):
    if n < 2:
        prime = False
    else:
        prime = True
        lim = int(math.sqrt(n))
        if n > 2 and n % 2 == 0:
            prime = False
        else:
            for i in range(3,lim+1):
                if n % i == 0:
                    prime = False
                    break
    return prime

def find_quad_cons_primes(lim):
    max_count = 0
    max_a = 0
    max_b = 0
    for a in range(-lim,lim+1):
        for b in range(-lim,lim+1):
            n = 0
            q = n ** 2 + a * n + b
            #if is_prime(q):
                #print("n^2 +",a,"n +",b,"=")
            while is_prime(q):
                #print(" n=",n,"=>",q)
                n += 1
                q = n ** 2 + a * n + b
            else:
                if n > max_count:
                    max_count = n
                    max_a = a
                    max_b = b
                    print("New primes count: a =",a,"b =",b,
                            "primes generated:",max_count)

    return max_a,max_b

def main():
    ARG_LEN = len(sys.argv)
    if ARG_LEN > 1:
        limit = int(sys.argv[1])
    else:
        limit = 42
    a,b = find_quad_cons_primes(limit)
    print("n^2 + a*n + b:")
    print("a =",a,", b =",b)
    print("a * b =",a*b)

if __name__ == '__main__':
    main()
