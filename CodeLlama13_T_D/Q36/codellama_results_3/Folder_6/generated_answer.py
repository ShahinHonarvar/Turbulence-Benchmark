
def filter_chars(string):
    return ''.join([char for char in string if ord(char) < 70 and ord(char) > 31])
