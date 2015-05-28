#!/usr/bin/python3.3

# Project Euler:
# Problem #22: Name Scores
#
# Using <names.txt>, a 46k text file containing over five-thousand first
# names, begin by sorting it into alphabetical order. Then working out the
# alphabetical value for each name, multiply this value by its alphabetical
# position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which
# is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
# COLIN would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?
#
# Answer:

import arrow
import datetime

def main():
    start = datetime.datetime(1901,1,1)
    end = datetime.datetime(2000,12,31)
    scount = 0
    for d in arrow.Arrow.range('day',start,end):
        if d.day == 1 and d.weekday() == 6:
            scount +=1
    print("Number of Sundays on 1st of month from",start.year,"to",end.year,":",scount)

if __name__ == '__main__':
    main()
