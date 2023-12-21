
import re

def return_nth_smallest_ascii(str):
    s = re.sub(r'[^A-z]', '', str)
    return s[12]
