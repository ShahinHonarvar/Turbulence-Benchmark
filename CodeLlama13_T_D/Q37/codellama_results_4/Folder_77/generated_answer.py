
def filter_chars(string):
    return ''.join([char for char in string if ord(char) < 384 or ord(char) > 411 or (ord(char) >= 57 and ord(char) <= 64)])
