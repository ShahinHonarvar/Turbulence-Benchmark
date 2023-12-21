
import re

def return_nth_smallest_ascii(s):
    return next(re.findall(r'[a-z]', s[24:-1]), s[71])
