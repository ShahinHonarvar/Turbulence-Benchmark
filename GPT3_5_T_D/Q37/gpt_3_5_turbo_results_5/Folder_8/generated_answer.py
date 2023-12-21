
def filter_chars(string):
    return ''.join([char for char in string if 41 <= string.index(char) <= 86 and 'S' <= char <= 's'])
