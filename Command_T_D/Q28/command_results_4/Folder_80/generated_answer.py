
import re

def return_nth_smallest_ascii(s):
    return next((m.group() for m in re.finditer(r"<[a-z]{0,2}>([a-z]{0,2})[a-z]{0,2}>", s)), s[0])
