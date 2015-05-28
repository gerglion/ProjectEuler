#!/usr/bin/python3.4

# Project Euler:
# Problem #19: Counting Sundays
#
# You are given the following information, but you may prefer to do some
# research for yourself.
#
# * 1 Jan 1900 was a Monday.
# * Thirty days has September,
#   April, June, and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
# * A leap year occurs on any year evenly divisible by 4, but not on a
#   century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?
#
# Answer: 171

import sys

MONTHS = [ "January",
           "February",
           "March",
           "April",
           "May",
           "June",
           "July",
           "August",
           "September",
           "October",
           "November",
           "December"
        ]
DAYS = [ "Sunday",
         "Monday",
         "Tuesday",
         "Wednesday",
         "Thursday",
         "Friday",
         "Saturday"
       ]
DAYS_PER_MONTH = [31,28,31,30,31,30,31,31,30,31,30,31]

def leap_year(yr):
    if( yr % 4 != 0 ):
        return False
    elif( yr % 100 != 0 ):
        return True
    elif( yr % 400 != 0 ):
        return False
    else:
        return True

def main():
    num_months = len(MONTHS)
    days_per_week = len(DAYS)
    start_year = 1901
    end_year = 2000
# Get to 1901
    year = 1900
    day_of_week = 0

    leap = leap_year(year)
    for mo in range(0,num_months):
        #print("Days in",MONTHS[mo],":",DAYS_PER_MONTH[mo])
        if(leap and mo == 1):
            dpm = 29
        else:
            dpm = DAYS_PER_MONTH[mo]
        for d in range(1,dpm+1):
            day_of_week = (day_of_week + 1) % days_per_week
        #print(DAYS[day_of_week],MONTHS[mo],d,year)
# Count 1st of month Sundays
    scount = 0
    for yr in range(start_year,end_year + 1):
        sc = 0
        leap = leap_year(yr)
        #if(leap):
            #print(" ** ",yr,"is leap year")
        for mo in range(0,num_months):
            if(leap and mo == 1):
                dpm = 29
            else:
                dpm = DAYS_PER_MONTH[mo]
            for d in range(1,dpm+1):
                day_of_week = (day_of_week + 1) % days_per_week
                #print(DAYS[day_of_week],MONTHS[mo],d,yr)
                if(day_of_week == 0 and d == 1):
                    #print(DAYS[day_of_week],MONTHS[mo],d,yr)
                    sc += 1
            #else:
                #if(leap and mo == 1):
                    #print("LEAP:",DAYS[day_of_week],MONTHS[mo],d,yr)
        else:
            #print(yr,"First Sundays:",sc)
            scount += sc
    print("Number of Sundays on 1st of month from",start_year,"to",end_year,":",scount)


if __name__ == '__main__':
    main()
