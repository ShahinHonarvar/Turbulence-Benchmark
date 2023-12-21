
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s[51:-1] if c), s[78])
