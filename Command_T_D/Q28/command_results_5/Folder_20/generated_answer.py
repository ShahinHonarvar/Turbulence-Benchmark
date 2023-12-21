
import re

def return_nth_smallest_ascii(s):
    m = re.search(r'[A-Z]{%d,%d}'.format(25, 64), s)
    return m.group(0)
