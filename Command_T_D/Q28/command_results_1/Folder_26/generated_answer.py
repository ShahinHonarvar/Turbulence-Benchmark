
import re

def return_nth_smallest_ascii(s):
    res = re.findall(r'[a-z]', s)[26]
    return res
