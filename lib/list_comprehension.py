#!/usr/bin/env python3

def return_evens(num_list):
    even = [num for num in num_list if num % 2 == 0]
    return even
# for num in num_list:
    #     if num % 2 == 0:
    #         num.append()


def make_exclamation(sentence_list):
    new_list = [i+"!" for i in sentence_list]
    return new_list

