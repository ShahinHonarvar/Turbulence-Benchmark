
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r"[A-Z]", s[34:-85]) if ord(c) == 20), None)
