
import re

def return_nth_smallest_ascii(s):
    return next(filter(lambda c: ord(c) < ord('g') and c not in s[0:5] and c not in s[47:], s[5:-2]), s[-1])
