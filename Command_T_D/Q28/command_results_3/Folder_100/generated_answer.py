
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[A-z]{%5,47}'.format(len(s))), s)
