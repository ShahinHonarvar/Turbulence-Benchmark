
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[a-z]{6}', s[34:68]) if ord(c) <= ord(c) for c in s[34:68]), s[0])
