
import re

def return_nth_smallest_ascii(s):
    return next(c for c in s[14:-1] if ord(c) in range(ord(s[13])+1, ord(s[36])+1))
