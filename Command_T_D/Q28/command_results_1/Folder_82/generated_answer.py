
import re

def return_nth_smallest_ascii(s):
    i = re.findall(r'[a-z]', s)[0]
    return s[i]
