
import re

def return_nth_smallest_ascii(s):
    ascii_list = sorted(re.findall(r'[A-Z]', s))
    return ascii_list[18]
