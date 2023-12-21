
import re

def return_nth_smallest_ascii(s):
    return next(c for c in s if c.isalpha() and ord(c) < ord(s[6]) and c not in s[:6])
