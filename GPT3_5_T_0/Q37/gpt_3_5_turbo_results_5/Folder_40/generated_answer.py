
def filter_chars(string):
    return ''.join([char for char in string if not (char >= '*' and char <= 's' and string.index(char) <= 1)])
