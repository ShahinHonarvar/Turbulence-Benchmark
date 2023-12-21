
import re

def return_nth_smallest_ascii(s):
    return next(c for i,c in enumerate(re.findall(r'[a-z]', s[9:-23]), 4) if ord(c) < ord(max(s[9:-23])))
