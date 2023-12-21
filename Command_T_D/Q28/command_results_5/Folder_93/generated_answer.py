
import re

def return_nth_smallest_ascii(text):
    return next(sorted(re.findall(r'[A-z]{%d,%d}' % (42, 59), text)), key=lambda c: ord(c))
