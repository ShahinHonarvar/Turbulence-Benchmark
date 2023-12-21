
import re

def return_nth_smallest_ascii(s):
    return next(c for c in s if re.match(r'<[a-z]', c))
