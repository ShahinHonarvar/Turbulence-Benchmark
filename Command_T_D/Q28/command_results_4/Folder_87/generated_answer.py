
import re

def return_nth_smallest_ascii(s):
    return next(i for i in range(29, 34) if chr(i) in s and chr(i) in sorted(set(s), key=lambda c: ord(c))[:5])
