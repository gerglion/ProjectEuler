#!/usr/bin/python3.4

# Project Euler:
# Problem #14: Longest Collatz Sequence
#
# The following iterative sequence is defined for the set of positive
# integers:
#
# n -> n/2    (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following
# sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# It can be seen that this sequence (starting with 13 and finishing with 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
# Answer: 837799 (chain length = 525)

import sys

collatz_chains = {1 : 1}
def find_collatz_chain(num):
    #print(" >Collatz:",num)
    if num in collatz_chains:
        #print(" <Chain:",collatz_chains[num])
        return collatz_chains[num]
    else:
        if num % 2 == 0:
            collatz_chains[num] = 1 + find_collatz_chain(num//2)
        else:
            collatz_chains[num] = 1 + find_collatz_chain(3 * num + 1)
        #print(" <Chain:",collatz_chains[num])
        return collatz_chains[num]

def find_longest_collatz(lim):
    longest_chain = 0
    longest_chain_i = 0
    for i in range(lim,1,-1):
        new_chain_length = find_collatz_chain(i)
        #print("Next:",i," : ",new_chain_length)
        if new_chain_length > longest_chain:
            longest_chain = new_chain_length
            longest_chain_i = i
            #print("New longest chain found!:",i,":",longest_chain)
    print("Longest Collatz chain: C(",longest_chain_i,") =",longest_chain)
    return longest_chain_i

def main():
    if len(sys.argv) > 1:
        limit = int(sys.argv[1])
    else:
        limit = 14
    collatz_chain_start = find_longest_collatz(limit)
    print("Longest Collatz chain under",limit," starts at:",collatz_chain_start)

if __name__ == '__main__':
    main()
