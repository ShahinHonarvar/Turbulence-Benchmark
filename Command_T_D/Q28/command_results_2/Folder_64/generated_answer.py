
import re

def return_nth_smallest_ascii(s):
    return re.findall(r'[a-z]', s)[-6]
