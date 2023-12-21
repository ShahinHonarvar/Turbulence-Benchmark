
import re

def return_nth_smallest_ascii(str_1):
    x = re.findall(r'[A-Z]', str_1)
    return sorted(set(x))[18]
