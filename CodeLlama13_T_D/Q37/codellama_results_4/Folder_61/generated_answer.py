
def filter_chars(string):
    return ''.join([char for char in string if (ord(char) < ord('G') or ord(char) > ord('p'))])
