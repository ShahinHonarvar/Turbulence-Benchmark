
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[a-z]', s[17:-1]) if ord(c) == 98), 'z')
