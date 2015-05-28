#!/usr/bin/python3.4

# Project Euler:
# Problem #17: Number Letter Counts
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used.
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
# 20 letters. The use of "and" when writing out numbers is in compliance with
# British usage.
#
# Answer: 21124

import sys

words = {}

def setup_num_word_dict():
    global words
    words['units'] = ['','one','two','three','four','five','six','seven',
                      'eight','nine']
    words['teens'] = ['','eleven','twelve','thirteen','fourteen','fifteen',
                      'sixteen','seventeen','eighteen','nineteen']
    words['tens'] = ['','ten','twenty','thirty','forty','fifty','sixty',
                      'seventy','eighty','ninety']

def count_series_letters(start,end):
    setup_num_word_dict()
    count = 0

    for i in range(start,end+1):
        num = i
        num_list = []
        num_string = ""

        while num > 0:
            num_list.append(num % 10)
            num = num // 10

        length = len(num_list)

        if length > 1:
            if num_list[1] == 1 and num_list[0] > 0:
                    num_string = words['teens'][num_list[0]]
            else:
                num_string = words['tens'][num_list[1]]
                if num_list[0] > 0 and num_list[1] > 0:
                    num_string += " " + words['units'][num_list[0]]
                else:
                    num_string +=  words['units'][num_list[0]]
            if length > 2 and num_list[2] > 0:
                if num_list[0] > 0 or num_list[1] > 0:
                    num_string = words['units'][num_list[2]] + \
                                 " hundred and " + num_string
                else:
                    num_string = words['units'][num_list[2]] + " hundred"
            if length > 3:
                num_string = words['units'][num_list[3]] + " thousand " +\
                num_string
        else:
            num_string = words['units'][num_list[0]]
        print(i,"has",length,length > 1 and "digits" or "digit")
        print(num_list[::-1])
        num_len = len(num_string.replace(" ",""))
        print(num_string,": has",num_len,"letters")
        count += num_len

    return count

def main():
    if len(sys.argv) > 1:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        assert start < end
    else:
        start = 1
        end = 5
    total_letters = count_series_letters(start,end)
    print("The numbers from",start,"to",end,"contain",total_letters,"letters.")

if __name__ == '__main__':
    main()
