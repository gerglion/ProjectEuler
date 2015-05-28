#!/usr/bin/python3.4

# Project Euler:
# Problem #25: Reciprocal Cycles
#
# A unit fraction contains 1 in the numerator. The decimal represenation of
# the unit fractions with denominators 2 to 10 are given:
#
#   1 / 2 = 0.5
#   1 / 3 = 0.(3)
#   1 / 4 = 0.25
#   1 / 5 = 0.2
#   1 / 6 = 0.1(6)
#   1 / 7 = 0.(142857)
#   1 / 8 = 0.125
#   1 / 9 = 0.(1)
#   1 / 10 = 0.1
#
# Where 0.1(6) means 0.1666666..., and has a 1-digit recurring cycle. It can
# be seen that 1 / 7 has a 6-digit recurring cycle.
#
# Find the value d < 1000 for which 1 / d contains the longest recurring
# cycle in its decimal fraction part.
#
# Answer: 983

import sys

def find_df_cycle(denominator):
    #print("Find cycle for:",1,"/",denominator)
    numerator = 10
    __N = 0
    __D = 1
    cycle = [[],[]]
    cycle_start = -1
    cycle_len = 0
    done = False
    pad = 0

    while numerator // denominator == 0:
        pad += 1
        numerator *= 10

    if numerator % denominator == 0:
        cycle[__N].append(numerator)
        cycle[__D].append(numerator//denominator)
    else:
        while not done and numerator not in set(cycle[__N]):
            if numerator % denominator == 0:
                done = True
                cycle[__D].append(numerator//denominator)
            elif numerator // denominator == 0:
                cycle[__N].append(numerator)
                cycle[__D].append(0)
                numerator *= 10
            else:
                dig = numerator // denominator
                cycle[__N].append(numerator)
                cycle[__D].append(dig)
                numerator = 10*(numerator % denominator)
        else:
            if numerator in set(cycle[__N]):
                for i in range(len(cycle[__N])):
                    if cycle[__N][i] == numerator:
                        cycle_start = i

    str_dig = "0."
    for i in range(pad):
        str_dig += "0"

    if cycle_start >= 0:
        cycle_len = len(cycle[__D]) - cycle_start
        for i in range(cycle_start):
            str_dig += str(cycle[__D][i])
        str_dig += "("
        for i in range(cycle_start,len(cycle[__D])):
            str_dig += str(cycle[__D][i])
        else:
            str_dig += ")"
    else:
        for i in range(len(cycle[__D])):
            str_dig += str(cycle[__D][i])

    #print(str_dig)

    return str_dig,cycle_len

def longest_df_cycle(start,end):
    l_cycle = 0
    l_cycle_d = 0
    for i in range(start,end+1):
        cycle,cycle_len = find_df_cycle(i)
        if cycle_len > l_cycle_d:
            l_cycle = cycle_len
            l_cycle_d = i
            #print("New longest cycle: 1 /",l_cycle_d,
            #        "=",cycle,"[",l_cycle,"]")
    return l_cycle_d

def main():
    ARG_LEN = len(sys.argv)
    if ARG_LEN > 1:
        df_limit = int(sys.argv[1])
    else:
        #df_limit = 1000
        df_limit = 10
    d = longest_df_cycle(2,df_limit)
    #find_df_cycle(df_limit)
    #print(check_cycle([0,6]))
    print("Longest recurring decimal cycle: 1 /",d)

if __name__ == '__main__':
    main()
