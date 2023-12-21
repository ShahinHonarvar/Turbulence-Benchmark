
import re

def return_nth_smallest_ascii(s):
    ascii = list(re.findall(r'[a-z]', s))
    ascii.sort()
    return ascii[3][-5]
