
def filter_chars(string):
    return ''.join([char for char in string if ord(char) < 51 or ord(char) > 96])
