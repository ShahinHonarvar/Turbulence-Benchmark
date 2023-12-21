
import re

def return_nth_smallest_ascii(s):
    return next(c for c in s[28:-2] if ord(c) < ord(s[15]))
