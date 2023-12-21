
import re

def return_nth_smallest_ascii(s):
    return next(re.findall(r'[a-z]', s[25:65]), s[0])
