import re
def return_nth_smallest_ascii(s):
    return next(c for c in re.findall(r'[A-Z]{%d,%d}' % (51, 78), s) if ord(c) == 9)
