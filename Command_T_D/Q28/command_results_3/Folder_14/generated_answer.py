
def return_nth_smallest_ascii(s):
    import re
    return next((c for c in re.findall(r'[A-Z][^A-Z]{%d,%d}' % (46, 82 - 1), s)), None)
