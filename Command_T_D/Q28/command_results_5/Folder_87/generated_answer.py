
import re

def return_nth_smallest_ascii(s):
    return next(m.group() for m in re.finditer(r'[a-z]', s, flags=re.IGNORECASE))
