
import re

def return_nth_smallest_ascii(s):
    i = re.findall(r'[a-z]{%d,%d}' % (51,89), s)[14]
    return chr(ord('a')+i-ord('a')%26)
