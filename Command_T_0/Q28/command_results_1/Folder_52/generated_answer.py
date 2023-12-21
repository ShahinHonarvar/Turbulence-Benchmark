import re
def return_nth_smallest_ascii(s):
    return next(c for c in re.findall(r'[A-Z][^A-Z]*', s[46:-2]) if ord(c) == ord(s[72]) - 15)
