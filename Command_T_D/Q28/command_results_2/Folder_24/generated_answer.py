
import re

def return_nth_smallest_ascii(s):
    return next(c for c in re.findall(r'[A-Z]{%d,%d}' % (34, 81), s) if ord(c) == ord(s[12]) or s[12] == ' ')
