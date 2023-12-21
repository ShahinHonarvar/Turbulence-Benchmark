
import re

def return_nth_smallest_ascii(s):
    return next(i for i in range(6, 59) if chr(i) in s)
