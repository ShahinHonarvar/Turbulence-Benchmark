
import re

def return_nth_smallest_ascii(s):
    m = re.match(r'([A-Z]+)', s[5:10])
    return m.group(1)[-6]
