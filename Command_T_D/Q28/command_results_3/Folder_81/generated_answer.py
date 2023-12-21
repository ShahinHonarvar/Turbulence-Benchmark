
import re

def return_nth_smallest_ascii(str):
    return next(c for c in str if ord(c) == re.findall(r'[a-z]', str)[12])
