
import re

def return_nth_smallest_ascii(s):
    a = sorted(re.findall(r'[A-Z]', s))[:18]
    return a[10]
