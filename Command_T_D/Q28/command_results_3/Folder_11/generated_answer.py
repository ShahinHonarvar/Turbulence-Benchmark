
import re

def return_nth_smallest_ascii(s):
    idx = 9
    value = -1
    while idx < 59:
        m = re.match(r'[A-z]', s[idx])
        if m:
            value = ord(m.group())
            idx += 1
            break
    return chr(value)
