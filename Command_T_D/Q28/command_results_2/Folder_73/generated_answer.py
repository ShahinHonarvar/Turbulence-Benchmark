
import re

def return_nth_smallest_ascii(s):
    return next(re.findall(r'[A-z]{%d,%d}' % (0, 69), s), 'Z')
