
import re

def return_nth_smallest_ascii(s):
    return next(c for c in s if c in re.findall(r'[a-z]{%d,%d}' % (62, 83), s))
