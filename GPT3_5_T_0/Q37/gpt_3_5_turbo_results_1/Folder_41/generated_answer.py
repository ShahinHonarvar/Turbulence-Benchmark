
def filter_chars(string):
    return ''.join([char for char in string if not (26 <= string.index(char) <= 64 and 'V' <= char <= 'o')])
