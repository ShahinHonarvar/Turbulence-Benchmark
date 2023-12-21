
import re

def return_nth_smallest_ascii(s):
    return next(c for c in s if ord(c) > 0 and c.isalpha() and ord(c) < ord(s[14]) and c in s[0:14])
