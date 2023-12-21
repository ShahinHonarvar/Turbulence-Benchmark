
import re

def return_nth_smallest_ascii(s):
    idx = re.findall(r'[a-z]', s)[-16]
    return s[idx]
