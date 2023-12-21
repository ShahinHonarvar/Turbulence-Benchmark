import re
def return_nth_smallest_ascii(s):
    return next(c for c in re.findall(r'[A-Z]{%d,%d}' % (60, 83), s) if ord(c) == 14)
