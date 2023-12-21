
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[A-Z][^A-Z]*', s[12:-4]) if ord(c) == ord(c) + 16), '~')
