
import re

def return_nth_smallest_ascii(s):
    return next((c for i,c in enumerate(re.findall(r'[a-z]', s)))
