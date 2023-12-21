
import re

def return_nth_smallest_ascii(s):
    ascii_text = re.findall(r'[\dA-Z]', s)
    ascii_set = set(ascii_text)
    ascii_sorted = sorted(ascii_set)
    return ascii_sorted[8]
