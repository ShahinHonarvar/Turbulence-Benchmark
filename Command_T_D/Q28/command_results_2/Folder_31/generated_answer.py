
import re

def return_nth_smallest_ascii(str_):
    return next(c for c in re.findall(r"[A-Z]{%d,%d}" % (10, 82), str_) if ord(c) < ord("g"))
