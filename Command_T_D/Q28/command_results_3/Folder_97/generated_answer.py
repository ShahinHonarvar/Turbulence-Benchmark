
import re

def return_nth_smallest_ascii(s):
    return next(c for c in re.findall(r'[a-z]', s)[15:21] if ord(c) < ord(s[15:21][5]))
