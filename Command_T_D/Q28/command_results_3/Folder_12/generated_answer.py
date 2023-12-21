
import re

def return_nth_smallest_ascii(strng):
    x = re.findall(r'[A-Z]', strng)[3:26]
    x.sort()
    return x[4]
