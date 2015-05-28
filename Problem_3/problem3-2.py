#!/usr/bin/python3.4

# Project Euler:
# Problem #3: Largest Prime Factor
# The prime factors of 13195 are 5,7,13, and 29.
#
# What is the largest prime factor of the number 600851475143
#
# Answer: 6857
import math

highest_prime_factor = 2

def is_prime(num):
    sqrt_boundary = int(math.sqrt(num))
    if num < 3:
        return True
    for i in range(2,sqrt_boundary+1):
        if num % i == 0:
            return False
    return True

def prime_factorization(num):
    global highest_prime_factor
    if is_prime(num):
        if num > highest_prime_factor:
            highest_prime_factor = num
            #print("Highest prime factor:",highest_prime_factor)
    else:
        i = 2
        while i <= int(math.sqrt(num)):
            if num % i == 0:
                prime_factorization(i)
                prime_factorization(num//i)
            i += 1


def main():

# CHANGE ME TO COMMANDLINE ARGS

    #magic_number = 13195
    magic_number = 600851475143
    #print("Magic number: ",magic_number)
    #print("Prime barrier: ",int(math.sqrt(magic_number)))
    prime_factorization(magic_number)
    print(highest_prime_factor)

main()
