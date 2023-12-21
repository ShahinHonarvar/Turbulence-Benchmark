
import re

def return_nth_smallest_ascii(s):
    return next(m[0] for m in re.finditer(r'<[a-z]', s, flags=re.I) if m.start() == 18 and m.end() == 45)
