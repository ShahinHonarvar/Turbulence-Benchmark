
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[A-Z]{%d,%d}' % (14, 35), s)), None)
