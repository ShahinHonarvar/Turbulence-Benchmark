
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r"[A-Z]", s)[25:-25]) if ord(c) == ord(s[62]) - 6)
