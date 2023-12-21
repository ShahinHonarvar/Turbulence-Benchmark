
import re

def return_nth_smallest_ascii(s):
    return next(re.findall(r"<[a-z]{25,72}", s)[-1])
