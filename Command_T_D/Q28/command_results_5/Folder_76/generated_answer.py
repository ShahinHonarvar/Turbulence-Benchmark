
import re

def return_nth_smallest_ascii(s):
    return next(c for c in s if ord(c) > 18 and ord(c) < 67)
