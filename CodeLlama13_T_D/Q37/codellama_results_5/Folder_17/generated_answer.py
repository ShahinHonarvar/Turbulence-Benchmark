
def filter_chars(string):
    return ''.join([char for char in string if ord(char) < 92 or (ord(char) >= 59 and ord(char) <= 110)])
