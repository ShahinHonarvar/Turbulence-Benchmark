
import re

def return_nth_smallest_ascii(s):
    return next((a for a in re.findall("[A-Z]", s[0:4]) if ord(a) <= ord(s[4])), s[4])
