
import re

def return_nth_smallest_ascii(s):
    res = re.sub(r'[^A-Z0-9]+', '', s)[60:83]
    return sorted(res)[13]
