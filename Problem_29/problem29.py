#!/usr/bin/python3.4

# Project Euler:
# Problem #29
#
# Answer:

import sys

def find_distinct_powers(lim):
    powers = set()
    #powers = {a ** b for a in range(2,lim+1) for b in range(2,lim+1)}
    for i in range(2,lim+1):
        for j in range(2,lim+1):
            powers.add(i ** j)
    #print(sorted(powers),"<<",len(powers),">>")
    return len(powers)
def main():
    ARG_LEN = len(sys.argv)
    if ARG_LEN > 1:
        limit = int(sys.argv[1])
    else:
        limit = 5
        #limit = 100
    ans = find_distinct_powers(limit)
    print("Distinct powers of a ^ b, 2 <= a <=",limit,", 2 <= b <=",limit,":",ans)

if __name__ == '__main__':
    main()
