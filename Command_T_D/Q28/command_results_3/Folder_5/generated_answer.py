
import re

def return_nth_smallest_ascii(s):
    idx = next(i for i in range(len(s)-5, -1, -1) if s[i] in re.findall(r'[a-z]', s[5:-5]))
    return s[idx]
