
import re

def return_nth_smallest_ascii(s):
    return next(c for c in re.findall(r'[A-z]', s, flags=re.I) if ord(c) in range(ord('A') + 24, ord('z') + 71))
