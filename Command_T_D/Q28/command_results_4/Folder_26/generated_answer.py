
import re

def return_nth_smallest_ascii(s):
    return next(c for c in s if type(c) == str and re.fullmatch(r"<[a-z]", c))
