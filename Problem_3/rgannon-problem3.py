#!/usr/bin/python3.4
import math

def is_prime(num):
    if num == 2 or num == 1:
        return True
    sqrt_num = math.ceil(math.sqrt(num)) + 1
    for i in range(2, int(sqrt_num)):
        if num % i == 0:
            return False

    return True

def prime_factors(num):
    if is_prime(num):
        return [num]

    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            ls = [i]
            return prime_factors(i) + prime_factors(num / i)
        i = i + 1

def main():
    factors = max(prime_factors(600851475143))
    print(factors)

main()
