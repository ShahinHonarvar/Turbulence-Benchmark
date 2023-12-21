
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s[5:-1] if c.isalpha() and ord(c) in range(ord('a') + 5, ord('z') + 89)), None)
