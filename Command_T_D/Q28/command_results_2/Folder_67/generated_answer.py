
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s[60:-14] if c in re.findall(r'[a-z]', s)), s[83])
