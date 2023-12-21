
import re

def return_nth_smallest_ascii(s):
    # insert your code here
    return next((c for c in s[10:90] if ord(c) in sorted(set(c))), s[0])
