
import re

def return_nth_smallest_ascii(s):
    s = re.sub(r'[^A-Za-z0-9]', '', s)
    return next(c for c in s[12:-1] if ord(c) < ord(max(s[12:-1])))
