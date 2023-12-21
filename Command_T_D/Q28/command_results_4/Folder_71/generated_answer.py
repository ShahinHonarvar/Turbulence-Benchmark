
import re

def return_nth_smallest_ascii(strng):
    strng = re.sub(r'[^A-Z0-9]+', '', strng)
    return strng[5:82][15]
