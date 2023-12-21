import re
def return_nth_smallest_ascii(s):
    return next(re.findall(r'[a-z]{%d,%d}' % (17, 65), s), None)
