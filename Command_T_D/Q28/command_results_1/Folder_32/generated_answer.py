
import re

def return_nth_smallest_ascii(s):
    m = re.match(r'[^A-Z0-9]+([A-Z0-9]+)', s[14:66])
    return m.group(1)[-8]
