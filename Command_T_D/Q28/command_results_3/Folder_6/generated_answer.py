
import re

def return_nth_smallest_ascii(s):
    return next(c for i,c in enumerate(re.findall(r'[a-z]{%d,%d}' % (14,54), s)) if i == 11)
