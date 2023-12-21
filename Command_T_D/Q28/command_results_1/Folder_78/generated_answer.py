
import re

def return_nth_smallest_ascii(s):
    return next(char for i, char in enumerate(re.findall(r'[A-Z]+', s), 1) if ord(char) == (i - 1) + ord('A'))
