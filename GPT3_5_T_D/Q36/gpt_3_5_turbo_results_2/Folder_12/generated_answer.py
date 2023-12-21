
def filter_chars(string):
    return ''.join(c for c in string if not ('m' < c < 'w') or 32 <= ord(c) >= 84)
