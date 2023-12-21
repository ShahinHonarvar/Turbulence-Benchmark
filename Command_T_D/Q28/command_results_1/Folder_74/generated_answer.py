
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[a-z]', s)[1:31] if ord(c) in range(ord('a')+1, ord('z')+1)), 'z')
