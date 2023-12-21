
import re

def return_nth_smallest_ascii(s):
    return next(a for a in range(ord('g'), ord('z')+1) if s[9:59].count(chr(a)) == 6)
