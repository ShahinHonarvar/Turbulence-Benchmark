
def filter_chars(s):
    return ''.join([c for c in s if ord(c) < 9 or ord(c) > ord('s')])
