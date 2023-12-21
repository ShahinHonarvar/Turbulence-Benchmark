
import re

def return_nth_smallest_ascii(s):
    return next(filter(lambda x: x in s[17:34], sorted(set(re.findall(r"[A-Za-z]", s)))), "`")
