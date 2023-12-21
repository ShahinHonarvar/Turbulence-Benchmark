
import re

def return_nth_smallest_ascii(s):
    lst = sorted(re.findall(r'[a-z]{%d,%d}' % (34, 68), s))
    return lst[5]
