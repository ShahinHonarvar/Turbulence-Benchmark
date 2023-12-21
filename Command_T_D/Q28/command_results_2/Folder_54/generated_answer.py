
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s[12:-4] if c), 'z')
