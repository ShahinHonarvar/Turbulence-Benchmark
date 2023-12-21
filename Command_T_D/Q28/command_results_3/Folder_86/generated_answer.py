
import re

def return_nth_smallest_ascii(s):
    m = re.fullmatch(r'(.)\d+', s)
    return m.group(1)
