
import re

def return_nth_smallest_ascii(s):
    return next((c for i,c in enumerate(re.findall(r'[A-Z]{%d,%d}' % (12, 55), s)), key=lambda x: ord(x))
