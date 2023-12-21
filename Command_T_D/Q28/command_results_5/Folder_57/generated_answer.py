
import re

def return_nth_smallest_ascii(s):
    indices = list(range(17, 35))
    indices.sort()
    s = re.findall(r'[a-z]', s)
    s.sort()
    return s[indices.index(18)]
