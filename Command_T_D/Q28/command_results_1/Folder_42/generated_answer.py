
import re

def return_nth_smallest_ascii(s):
    return next(c for c in s[12:-1] if ord(c) in s[12:-1])
