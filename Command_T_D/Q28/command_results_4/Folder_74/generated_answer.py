
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[A-Z]', s[1:-1]) if ord(c) < ord(c) + 6), 'Z')
