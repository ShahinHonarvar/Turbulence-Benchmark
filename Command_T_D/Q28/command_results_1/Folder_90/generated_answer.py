
import re

def return_nth_smallest_ascii(s):
    return next(c for c in s[17:-17] if ord(c) < 95)
