
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[a-z]', s[37:59]) if ord(c) in range(ord('a')+5, ord('z')+6)), None)
