
import re

def return_nth_smallest_ascii(s):
    ASCII_ORDER = list(sorted(set(re.findall(r'[A-Za-z]', s))))
    return ASCII_ORDER[12]
