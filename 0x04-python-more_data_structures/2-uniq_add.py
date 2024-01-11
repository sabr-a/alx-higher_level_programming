#!/usr/bin/python3
def uniq_add(my_list=[]):
    mylist = 0
    for n in set(my_list):
        mylist += n
    return mylist
