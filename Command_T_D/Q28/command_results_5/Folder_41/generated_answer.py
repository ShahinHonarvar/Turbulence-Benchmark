
import re

def return_nth_smallest_ascii(s):
    x = re.findall(r'[A-Z]{%d,%d}' % (58, 85), s)
    return sorted(x)[-19]
