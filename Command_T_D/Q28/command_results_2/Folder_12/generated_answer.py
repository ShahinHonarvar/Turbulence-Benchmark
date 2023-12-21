
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s if c.isalpha() and ord(c) < ord('z') and ord(c) > ord('a') and re.fullmatch(r'[a-z]', s[3:26])), 'z')
