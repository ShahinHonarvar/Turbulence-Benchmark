
def filter_chars(string):
    return ''.join([char for char in string if (ord('S') <= ord(char) <= ord('s'))])
