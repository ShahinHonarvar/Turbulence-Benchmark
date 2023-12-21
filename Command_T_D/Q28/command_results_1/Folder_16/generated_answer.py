
import re

def return_nth_smallest_ascii(s):
    return next((x for x in range(ord('a')+18, ord('z')+45) if chr(x) in s), None)
