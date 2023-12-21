
import re

def return_nth_smallest_ascii(s):
    for m in re.finditer(r'[a-z]', s):
        if ord(m.group()) >= 52 and ord(m.group()) <= 79:
            return m.group()
    return s[52]
