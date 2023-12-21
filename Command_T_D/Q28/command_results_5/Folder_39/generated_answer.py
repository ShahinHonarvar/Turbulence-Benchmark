
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s[1:-1] if ord(c) <= ord('z') - 8), 'z')
