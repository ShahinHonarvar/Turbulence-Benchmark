
def filter_chars(string):
    return ''.join([char for char in string if ord(char) < 283 or ord(char) > 484])
