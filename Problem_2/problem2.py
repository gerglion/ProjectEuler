#!/usr/bin/python3.4

# Project Euler:
# Problem #2: Even Fibonacci Numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even valued terms.
#
# Answer: 4613732

first = 1
second = 2
fib_sum = second
fib = first + second
while fib < 4000000:
    if fib % 2 == 0:
        fib_sum += fib
    first = second
    second = fib
    fib = first + second

print(fib_sum)

