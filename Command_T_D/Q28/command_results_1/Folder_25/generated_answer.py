
import re

def return_nth_smallest_ascii(s):
    return next((x for x in s[34:-2] if ord(x) < ord(s[34])), s[34])
