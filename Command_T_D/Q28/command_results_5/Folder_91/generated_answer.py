
import re

def return_nth_smallest_ascii(s):
    r = re.sub(r'[^A-z0-9]', '', s)
    c = sorted(r)[:8]
    return c[7]
