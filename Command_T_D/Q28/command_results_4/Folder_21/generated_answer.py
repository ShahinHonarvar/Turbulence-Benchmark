
import re

def return_nth_smallest_ascii(s):
    res = next(re.finditer(r'[a-z]{8,65}', s))[0]
    return res
