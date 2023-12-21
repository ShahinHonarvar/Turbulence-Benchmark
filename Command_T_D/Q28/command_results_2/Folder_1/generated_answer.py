
import re

def return_nth_smallest_ascii(s):
    return next(c for c in re.findall(r"[a-z]{%d,%d}" % (21, 59), s) if ord(c) == 11)
