import re
def return_nth_smallest_ascii(s):
    return next(c for c in re.findall(r'[A-Z]', s) if ord(c) > 32 and ord(c) < 68)
