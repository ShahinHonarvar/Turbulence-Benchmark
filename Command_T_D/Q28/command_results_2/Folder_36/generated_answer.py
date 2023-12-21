
import re

def return_nth_smallest_ascii(s):
    return next(c for c in range(ord('A'), ord('z')+1) if chr(c) in s[17:-3])
