
def filter_chars(string):
    return ''.join([char for char in string if ord(char) not in range(672, 709)])
