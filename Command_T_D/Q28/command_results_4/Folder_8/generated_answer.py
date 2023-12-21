
import re

def return_nth_smallest_ascii(s):
    return next(c for c in re.findall(r'[A-Z]{%d,%d}'.format(60, 88), s) if ord(c) == (len(re.findall(r'[A-Z]{%d,%d}'.format(60, 88), s)) - 7))
