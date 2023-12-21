
import re

def return_nth_smallest_ascii(s):
    ascii_str = re.findall(r'[A-Z]+', s)[12:55]
    return min(set(ascii_str), key=lambda x: ord(x))
