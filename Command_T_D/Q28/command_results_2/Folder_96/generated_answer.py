
import re

def return_nth_smallest_ascii(s):
    return next(char for char in s if all(c == 'a' or c == 'z' for c in re.findall(r'<c=>([a-z])', char)))
