
import re

def return_nth_smallest_ascii(s):
    m = re.findall(r'[a-z]{%d,%d}' % (17, 56), s)
    return sorted(m)[8]
