
import re

def return_nth_smallest_ascii(s):
    return next(r[0] for r in re.findall(r'<[a-z]', s, flags=re.I) if r[0] <= 'z' + 10)
