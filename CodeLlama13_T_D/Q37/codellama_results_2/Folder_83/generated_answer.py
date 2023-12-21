
def filter_chars(string):
    return ''.join([char for char in string if 29 <= ord(char) <= 79 and ord('K') <= ord(char) <= ord('z')])
