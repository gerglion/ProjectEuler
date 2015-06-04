#!/usr/bin/python3.4

# Project Euler:
# Problem #30:
#
# Answer: 443839

import sys

def list_digits(num):
    digs = []
    n = num
    while n > 0:
        digs.append(n%10)
        n = n // 10
    return digs

def find_range(exp):
    max_dig = 9 ** exp
    dig = 1
    while int(dig*"9")<dig*max_dig:
        dig +=1
    return max_dig * dig

def find_narc_numbers(exp):
    ran = find_range(exp)
    val = []
    for i in range(10):
        val.append(i ** exp)

    narc = []
    for i in range(2,ran):
        lst = list_digits(i)
        exp_lst = [val[x] for x in lst]
        if sum(exp_lst) == i:
           narc.append(i)
    return narc

def main():
    ARG_LEN = len(sys.argv)
    if ARG_LEN > 1:
        exp = int(sys.argv[1])
    else:
        exp = 4

    ans = find_narc_numbers(exp)
    print("Sum:",ans,"=",sum(ans))

if __name__ == '__main__':
    main()
