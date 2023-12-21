
import re

def return_nth_smallest_ascii(s):
    return next(a for i,a in enumerate(sorted(re.findall(r'[a-z]{%d,%d}' % (8, 26), s)), key=lambda x: ord(x)) if i == 6)
