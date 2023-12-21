
import re

def return_nth_smallest_ascii(s):
    return next(r[0] for r in re.finditer(r'[a-z]', s))
