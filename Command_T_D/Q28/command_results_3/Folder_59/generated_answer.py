
import re

def return_nth_smallest_ascii(s):
    return next(filter(str.isdigit, re.findall(r'[0-9]', s)), '0')
