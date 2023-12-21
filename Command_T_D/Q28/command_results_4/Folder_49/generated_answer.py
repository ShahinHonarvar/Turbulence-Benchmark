
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s[20:-20] if ord(c) < ord(s[11])), s[11])
