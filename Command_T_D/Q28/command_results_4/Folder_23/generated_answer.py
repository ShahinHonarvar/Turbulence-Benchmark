
import re

def return_nth_smallest_ascii(s):
    idx = re.findall(r'[A-Z]', s)[29:47]
    idx.sort()
    return idx[6]
