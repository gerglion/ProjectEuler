#!/usr/bin/python3.4

# Project Euler:
# Problem #1: Multiples of 3 and 5
# If we list all of the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6, and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Answer: 233168

sum = 0
for count in range(1000):
    if count % 5 == 0 or count % 3 == 0:
        sum += count

print(sum)
