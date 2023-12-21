
import re

def return_nth_smallest_ascii(s):
    return next(char for char in re.findall(r'[A-Z]{%d,68}' % (28,), s))
