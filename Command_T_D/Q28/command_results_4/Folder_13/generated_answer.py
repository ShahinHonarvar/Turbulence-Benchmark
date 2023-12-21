
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[a-z]{%d,%d}' % (47, 80), s) if ord(c) < ord(c) for c in s), None)
