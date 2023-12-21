
import re

def return_nth_smallest_ascii(s):
    return re.findall(r'[A-Z]', s)[7]
