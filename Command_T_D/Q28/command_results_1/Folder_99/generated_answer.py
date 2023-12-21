
import re

def return_nth_smallest_ascii(s):
    return next(c for c in re.findall(r'[A-Z]{%s:%s}'.format(17, 65), s))
