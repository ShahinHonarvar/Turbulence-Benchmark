
import re

def return_nth_smallest_ascii(s):
    m = re.findall(r'[a-z]', s)[20:80]
    return sorted(set(m))[10]
