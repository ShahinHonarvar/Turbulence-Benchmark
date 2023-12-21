
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s if 0 <= ord(c) - ord('a') <= 13), 'a')
