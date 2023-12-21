
def filter_chars(string):
    return ''.join([c for c in string if ord(c) not in range(ord('S'), ord('m'))])
