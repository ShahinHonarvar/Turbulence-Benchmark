import sys
def return_n_smallest_chars(s):
    s += " " * len(s)
    s += s[::-1]
    return s[:79]
