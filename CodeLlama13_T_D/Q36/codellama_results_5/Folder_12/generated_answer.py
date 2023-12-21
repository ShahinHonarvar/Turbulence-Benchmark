
def filter_chars(s):
    # Remove all characters between 32 and 84 (both exclusive)
    # that are greater than 'm' and smaller than 'w' in the string
    s = ''.join([c for c in s if not (ord('m') < ord(c) < ord('w'))])
    return s
