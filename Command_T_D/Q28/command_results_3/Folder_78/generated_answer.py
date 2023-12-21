
import re

def return_nth_smallest_ascii(s):
    return next(c for c in re.findall(r'[a-z]', s) if ord(c) < 89)
