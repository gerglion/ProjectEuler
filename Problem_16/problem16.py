#!/usr/bin/python3.4

# Project Euler:
# Problem #16: Power Digit Sum
#
# 2 ^ 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2 ^ 1000?
#
# Answer: 1366

import sys
def sum_digits(base,power):
    the_number = base ** power
    dig_list = []
    #print("Exponent:",the_number)
    while the_number > 0:
        dig = the_number % 10
        the_number = the_number // 10
        dig_list.append(dig)
    #print(dig_list[::-1])
    return sum(dig_list)

def main():
    if len(sys.argv) > 1:
        base = int(sys.argv[1])
        power = int(sys.argv[2])
    else:
        base = 2
        power = 15
    digit_sum = sum_digits(base,power)
    print("Sum of digits of",base,"^",power,":",digit_sum)

if __name__ == '__main__':
    main()
