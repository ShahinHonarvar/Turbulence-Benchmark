
def filter_chars(string):
    return ''.join([char for char in string if ord(char) < 123 and ord(char) > 76])
