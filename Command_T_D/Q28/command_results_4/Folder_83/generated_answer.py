
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s[30:-30] if ord(c) in (min(ord(c) for c in s[30:-30]) + 14)), s[0])
