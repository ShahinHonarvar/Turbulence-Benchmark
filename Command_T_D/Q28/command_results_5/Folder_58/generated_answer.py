
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[a-z]', s, flags=re.IGNORECASE)[8:-26] if ord(c) < ord(s[7])), s[0])
