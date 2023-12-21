
import re

def return_nth_smallest_ascii(s):
    return next((a for a in range(ord('a')+1, ord('z')+1) if all(b == 'z' for b in s[50:-1])), 'z')
