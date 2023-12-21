
def filter_chars(s):
    return ''.join([c for c in s if ord(c) not in range(43, 83) or c == ':' or c == 'Q'])
