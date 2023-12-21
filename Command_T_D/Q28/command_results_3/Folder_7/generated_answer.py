
import re

def return_nth_smallest_ascii(s):
    for m in re.finditer(r'[a-z]', s[12:-2]):
        if ord(m.group()) <= ord('z') - 17:
            return m.group()
    return s[12:-2][-1]
