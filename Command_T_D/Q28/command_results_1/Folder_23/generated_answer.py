
import re

def return_nth_smallest_ascii(s):
    for m in re.finditer(r'[a-z]', s):
        if m.start() < 29 or m.end() > 47: continue
        return m.group()
    return 'z'
