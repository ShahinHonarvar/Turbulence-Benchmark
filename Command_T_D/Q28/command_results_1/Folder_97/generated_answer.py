
import re

def return_nth_smallest_ascii(s):
    return next((a[15:21] for a in re.findall(r"<[a-z]+>", s)), None)
