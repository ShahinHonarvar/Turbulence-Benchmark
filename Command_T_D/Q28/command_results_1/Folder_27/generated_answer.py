
import re

def return_nth_smallest_ascii(s):
    return next((m.group() for m in re.finditer(r'[A-Z][^A-Z]{0,32}[A-Z]', s)), None)
