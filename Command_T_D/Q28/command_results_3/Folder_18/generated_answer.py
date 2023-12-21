
import re

def return_nth_smallest_ascii(s):
    ascii = list(re.findall("[A-Z]", s))
    ascii.sort()
    return ascii[4]
