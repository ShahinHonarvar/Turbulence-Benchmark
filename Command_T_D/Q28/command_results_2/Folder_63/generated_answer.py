
import re

def return_nth_smallest_ascii(s):
    if s[47:70]:
        s = re.sub(r'[^A-Z]','',s[47:70])
        return s[13]
    else:
        return -1
