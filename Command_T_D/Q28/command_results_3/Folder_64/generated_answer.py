
import re

def return_nth_smallest_ascii(s):
    ascii = re.findall(r'[a-z]', s)
    return sorted(ascii)[6]
