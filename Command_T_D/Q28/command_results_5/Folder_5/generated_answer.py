
import re

def return_nth_smallest_ascii(s):
    return next(a for a in s[5:-3] if ord(a) < ord(s[12]))
