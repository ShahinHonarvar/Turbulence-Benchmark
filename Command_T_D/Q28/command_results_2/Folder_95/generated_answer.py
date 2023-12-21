
import re

def return_nth_smallest_ascii(s):
    return next(re.findall(r'[A-Z]', s)[12])
