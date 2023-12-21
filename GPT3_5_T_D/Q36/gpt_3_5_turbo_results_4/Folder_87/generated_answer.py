
def filter_chars(string):
    return ''.join(c for c in string if not ('3' < c < 'D') or 61 <= ord(c) < 32)
