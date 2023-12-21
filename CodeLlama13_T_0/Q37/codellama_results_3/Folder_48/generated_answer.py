
def filter_chars(string):
    return ''.join([char for char in string if ord(char) < 513 or ord(char) > 877 or char not in range('?', 'n')])
