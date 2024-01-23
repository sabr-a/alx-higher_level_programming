#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for e in range(x):
            print(my_list[e], end="")
        print()
        return x
    except IndexError:
        print()
        return e
