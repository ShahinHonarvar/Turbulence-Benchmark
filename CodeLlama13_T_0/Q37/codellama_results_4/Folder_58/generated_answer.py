
def filter_chars(string):
    return ''.join([char for char in string if ord(char) < 503 or ord(char) > 753 or (ord(char) >= 9 and ord(char) <= 122)])
