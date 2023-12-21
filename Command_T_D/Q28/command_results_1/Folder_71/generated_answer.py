
import re

def return_nth_smallest_ascii(s):
    return next(r[1] for r in re.findall(r'<\d+>(\D)', s))
