
import re

def return_nth_smallest_ascii(s):
    match = re.search(r'[A-z]{%d,%d}'.format(38, 64), s)
    return match.group()
