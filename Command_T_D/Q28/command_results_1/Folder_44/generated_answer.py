
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s[20:-30] if ord(c) < 8), None)
