
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[A-Z]', s[67:77]) if ord(c) < ord('M') ), 'Z')
