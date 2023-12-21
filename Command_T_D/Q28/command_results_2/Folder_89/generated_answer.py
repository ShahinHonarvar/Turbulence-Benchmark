
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[A-Z]', s[24:-24]) if ord(c) == (i+24) % 95), None)
