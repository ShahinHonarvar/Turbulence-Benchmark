
def filter_chars(string):
    return ''.join([char for char in string if not (char > '+' and char < 'w' and 56 <= string.index(char) < 86)])
