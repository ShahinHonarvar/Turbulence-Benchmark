
import re

def return_nth_smallest_ascii(str):
    return next(re.findall(r'[A-z]{%d,%d}' % (52, 79), str))
