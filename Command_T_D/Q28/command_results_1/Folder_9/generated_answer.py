
import re

def return_nth_smallest_ascii(s):
    r = re.findall(r'[a-z]{%d,%d}'.format(10, 90), s)
    return min(r, key=lambda x: ord(x))
