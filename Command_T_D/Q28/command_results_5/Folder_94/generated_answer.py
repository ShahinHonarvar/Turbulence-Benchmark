
import re

def return_nth_smallest_ascii(s):
    return next(re.findall(r'[A-Z][^A-Z]*[A-Z]', s)[19])
