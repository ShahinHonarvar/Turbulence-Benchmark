
def filter_chars(string):
    return ''.join(char for char in string if not (29 <= string.index(char) <= 79 and 'K' <= char <= 'z'))
