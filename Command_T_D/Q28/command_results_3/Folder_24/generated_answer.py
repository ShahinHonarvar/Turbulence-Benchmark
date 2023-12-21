
import re

def return_nth_smallest_ascii(s):
    idx = re.findall(r'[a-z]', s)[-30:-1]
    idx.sort()
    idx = idx[:12]
    return idx[34]
