
def filter_chars(string):
    return ''.join([char for char in string if ord(char) < 123 or (ord(char) > 57 and ord(char) < 90)])
