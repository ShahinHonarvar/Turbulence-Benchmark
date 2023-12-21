
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s[30:-30] if ord(c) < ord(s[60])), s[70])
