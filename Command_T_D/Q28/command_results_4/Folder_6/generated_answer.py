
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s[14:-3] if ord(c) < 112), s[53])
