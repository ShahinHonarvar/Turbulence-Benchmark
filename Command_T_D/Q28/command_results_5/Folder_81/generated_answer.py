
import re

def return_nth_smallest_ascii(s):
    return next(re.findall(r"<(.)>", s), None)
