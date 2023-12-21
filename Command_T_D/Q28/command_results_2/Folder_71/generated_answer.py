
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[A-Z]', s)[5:-3]) if ord(c) == chr(ord('A') + 15))
