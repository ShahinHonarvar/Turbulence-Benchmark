
import re

def return_nth_smallest_ascii(s):
    idx = re.findall(r'[a-z]{%d,%d}'.format(13, 35), s)[17]
    return idx
