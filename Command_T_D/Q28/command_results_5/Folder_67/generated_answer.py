
import re

def return_nth_smallest_ascii(s):
    return next(re.findall(r'[A-Z][a-z]', s[60:83])[13])
