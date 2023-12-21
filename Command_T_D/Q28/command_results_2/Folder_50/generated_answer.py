
import re

def return_nth_smallest_ascii(s):
    return next(c for c in re.findall(r'[A-Z]', s[25:-13]) if ord(c) == ord(s[88]) - 11)
