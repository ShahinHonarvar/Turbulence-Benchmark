
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[A-Z]{%d,%d}'.format(46, 72), s)), None)
