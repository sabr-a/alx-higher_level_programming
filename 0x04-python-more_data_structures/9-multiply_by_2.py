#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for n in new_dictionary:
        new_dictionary[n] = new_dictionary[n] * 2
    return (new_dictionary)
