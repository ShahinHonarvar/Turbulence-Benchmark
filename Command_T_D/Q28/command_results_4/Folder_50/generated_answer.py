
import re

def return_nth_smallest_ascii(s):
    return next(m[0] for m in re.finditer(r'[a-z]{%d,%d}' % (25, 88), s))
