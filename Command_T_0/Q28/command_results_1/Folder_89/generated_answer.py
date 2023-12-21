import re
def return_nth_smallest_ascii(s):
    return next(re.findall(r'[A-Z]{%d,%d}'.format(24, 71), s))
