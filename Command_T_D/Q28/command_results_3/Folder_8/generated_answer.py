
import re

def return_nth_smallest_ascii(s):
    ascii_re = re.compile(r'[A-Z]')
    return next((c for c in ascii_re.findall(s, 60, 88) if ord(c) in range(ord('A'), ord('Z') + 1, 7)), None)
