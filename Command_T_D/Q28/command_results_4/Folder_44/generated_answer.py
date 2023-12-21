
import re

def return_nth_smallest_ascii(s):
    ascii = sorted(re.findall(r'[a-z]', s[20:-10]))
    return ascii[7]
