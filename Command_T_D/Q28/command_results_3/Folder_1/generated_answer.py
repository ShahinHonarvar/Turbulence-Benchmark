
import re

def return_nth_smallest_ascii(s):
    m = re.search(r'[a-z]+', s[21:59])
    return next(c for c in m.group() if ord(c) == 11)
