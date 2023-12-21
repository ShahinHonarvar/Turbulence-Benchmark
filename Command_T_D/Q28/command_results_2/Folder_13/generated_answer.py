
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s[47:-1] if ord(c) in range(49, 81)), s[47])
