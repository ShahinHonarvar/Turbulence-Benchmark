
import re

def return_nth_smallest_ascii(s):
    str_re = re.compile(".*[a-z].*")
    m = str_re.search(s)
    if m:
        c = ord(m.group())
        return s[c-60:c+14]
    else:
        return None
