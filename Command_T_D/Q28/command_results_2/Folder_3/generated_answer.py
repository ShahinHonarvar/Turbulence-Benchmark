
import re

def return_nth_smallest_ascii(s):
    return next(c for c in re.findall(r'[A-z]{%d,%d}' % (25, 45), s))
