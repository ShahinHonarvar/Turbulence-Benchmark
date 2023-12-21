
import re

def return_nth_smallest_ascii(s):
    return next(c for c in s[28:-1] if c.isalpha() and c.isupper() and ord(c) in range(ord("A") + 14, ord("Z") - 1))
