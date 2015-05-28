#!/usr/bin/python3.4

# Project Euler:
# Problem #15: Lattice Paths
#
# Starting from the top left corner of a 2x2 grid, and only being able to
# move to the right and down, there are exactly 6 routes to the bottom
# right corner.
#
# How many such routes are there through a 20x20 grid?
#
# Answer: 137846528820

import sys
def find_paths(side,path):
    if len(path) == 2 * side:
        #print(path)
        return 1
    else:
        if path.count('R') < side and path.count('D') < side:
            return find_paths(side,path+"R") + find_paths(side,path+"D")
        elif path.count('R') < side:
            return find_paths(side,path+"R")
        else:
            return find_paths(side,path+"D")

def count_paths(side):
    return 2 * find_paths(side,"R")

def main():
    if len(sys.argv) > 1:
        side_length = int(sys.argv[1])
    else:
        side_length = 3
    total_paths = count_paths(side_length)
    print("Valid paths for a grid with side length of",side_length,":",total_paths, "out of",2**(2*side_length))

if __name__ == '__main__':
    main()
