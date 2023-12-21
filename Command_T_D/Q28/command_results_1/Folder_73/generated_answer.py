
import re

def return_nth_smallest_ascii(s):
    return next((char for char in range(ord('a') + 1, ord('z') + 1) if all(c > char for c in range(ord('a') + 1, ord('z') + 1)) for char in re.findall(r'[a-z]', s)), 'z')
