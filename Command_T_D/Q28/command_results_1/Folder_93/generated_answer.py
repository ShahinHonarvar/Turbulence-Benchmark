
import re

def return_nth_smallest_ascii(s):
    ascii = list(sorted(re.findall(r'[a-z]', s[42:59])))
    return ascii[16]
