import re
def return_nth_smallest_ascii(s):
    return next(c for c in s if c.isalpha() and ord(c) < ord('g') and c.isupper() and c.islower() and c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
