
def filter_chars(string):
    return ''.join([char for char in string if (ord(char) < ord('s') or ord(char) > ord('S'))])
