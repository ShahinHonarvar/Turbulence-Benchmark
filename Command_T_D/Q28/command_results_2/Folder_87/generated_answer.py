
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s[29:-1] if ord(c) < ord(s[33])), s[33])
