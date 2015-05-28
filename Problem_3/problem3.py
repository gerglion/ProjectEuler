#!/usr/bin/python3.4

# Project Euler:
# Problem #3: Largest Prime Factor
# The prime factors of 13195 are 5,7,13, and 29.
#
# What is the largest prime factor of the number 600851475143
#
# Answer: 6857
import math

def generate_primes(max):
    primes = [2]
    for i in range(2,max+1):
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def prime_factorization(num):
    primes = generate_primes(int(math.sqrt(num)))
    print("primes done")
    top_prime_factor = 0
    for i in primes[::-1]:
        if num % i == 0:
            top_prime_factor = i
            break
    return top_prime_factor

def main():
    #magic_number = 13195
    magic_number = 600851475143
    print("Magic number: ",magic_number)
    print("Prime barrier: ",int(math.sqrt(magic_number)))
    top_prime_factor = prime_factorization(magic_number)
    print(top_prime_factor)

main()
