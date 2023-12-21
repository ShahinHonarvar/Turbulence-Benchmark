
import re

def return_nth_smallest_ascii(s):
    str1 = re.sub(r'[^A-Z]', '', s)
    return str1[13]
