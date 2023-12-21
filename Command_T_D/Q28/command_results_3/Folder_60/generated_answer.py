
import re

def return_nth_smallest_ascii(str):
    return next(re.findall(r'[a-z]{%d,%d}' % (36, 79), str), -1)
