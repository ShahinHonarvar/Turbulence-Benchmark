
import re

def return_nth_smallest_ascii(str):
    return next((c for c in re.findall(r'[a-z]', str, flags=re.I) if ord(c) >= 46 and ord(c) <= 82), 'z')
