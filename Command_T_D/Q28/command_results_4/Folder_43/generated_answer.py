
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[a-z]', s[14:-4]) if ord(c) == ord(s[14]) + 10), s[14])
