
import re

def return_nth_smallest_ascii(s):
    lst = sorted(re.findall(r'[A-Z]', s))
    return lst[6]
