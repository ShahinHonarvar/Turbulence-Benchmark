
import re

def return_nth_smallest_ascii(s):
    i = 47
    j = 70
    while i < j:
        idx = s.find(chr(i), i, j)
        if idx != -1:
            return chr(i)
        i += 1
    return chr(j)
