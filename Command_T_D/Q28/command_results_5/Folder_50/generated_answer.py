
import re

def return_nth_smallest_ascii(s):
    ascii_re = re.compile(r'[A-Z]')
    ascii_str = ''.join(re.findall(ascii_re, s))
    return ascii_str[25][10]
