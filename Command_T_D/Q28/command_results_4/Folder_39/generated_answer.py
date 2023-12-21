
import re

def return_nth_smallest_ascii(s):
    return next(c for c in re.findall(r'[A-z]{%d,%d}' % (1, 66), s) if ord(c) % 8 == 7)
