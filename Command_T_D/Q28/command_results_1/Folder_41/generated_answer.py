
import re

def return_nth_smallest_ascii(s):
    ascii_re = re.compile(r'[A-Z]+')
    m = ascii_re.finditer(s, flags=re.IGNORECASE)
    return next(a[1] for i,a in enumerate(sorted(list(zip(*m)))))
