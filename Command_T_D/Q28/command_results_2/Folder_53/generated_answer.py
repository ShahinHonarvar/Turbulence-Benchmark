
import re

def return_nth_smallest_ascii(s):
    return next(i for i in range(40, 61) if chr(i) in s and chr(i) in sorted(set(re.findall(r'[A-Z]', s)), key=lambda c: ord(c)))
