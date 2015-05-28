#!/usr/bin/python3.4

# Project Euler:
# Problem #4: Largest Palindrome Product
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer: 906609

import math
import sys

def is_palindrome(num):
    digits = get_digit_length(num)
    i = 0
    #print("Testing:",num)
    while i < (((digits - i)-1)):
        r_num = get_digit(num,i)
        l_num = get_digit(num,((digits - i)-1))
        if l_num != r_num:
            return False
        i += 1
    #print("YES!!",num)
    return True


def fill_number(num,digits):
    number = num
    for i in range(1,digits):
        number += num * (10 ** i)
    return number


def get_digit(num,digit):
    dig = 0
    n = num
    for i in range(0,digit+1):
        dig = n % 10
        n = (n - dig)//10
    return dig


def get_digit_length(num):
    if num > 0:
        digits = int(math.log10(num))+1
    elif n == 0:
        digits = 1
    else:
        digits = int(math.log10(-num))+1
    return digits


def palin_search(digits):
    cur_top_i = 0
    cur_top_j = 0
    boundary = fill_number(9,digits)
    cur_top_palin = 0
    for i in range(boundary,0,-1):
        for j in range(i,0,-1):
            ppalin = i * j
            if is_palindrome(ppalin) and ppalin > cur_top_palin:
                cur_top_i = i
                cur_top_j = j
                cur_top_palin = ppalin
    return cur_top_i,cur_top_j,cur_top_palin


def main():
    if len(sys.argv) > 1:
        dig = int(sys.argv[1])
        if isinstance(dig,int) and dig > 0:
            digits = dig
        else:
            digits = 3
    else:
        digits = 3
    i,j,answer = palin_search(digits)
    print("Largest palindrome integer for",digits,"digit numbers:",i,"*",j,"=",answer)

main()
