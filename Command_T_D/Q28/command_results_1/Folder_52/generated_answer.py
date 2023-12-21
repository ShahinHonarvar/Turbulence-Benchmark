
import re

def return_nth_smallest_ascii(str):
    return next((c for c in str if c.isalpha() and c.isupper() and ord(c) > 64 and ord(c) < 73), None)
