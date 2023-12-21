
def filter_chars(string):
    return ''.join([char for char in string if not (ord('5') <= ord(char) <= ord('_'))])
