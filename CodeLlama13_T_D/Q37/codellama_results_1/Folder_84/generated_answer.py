
def filter_chars(string):
    return ''.join([char for char in string if (ord(char) < 138 or ord(char) > 920) and (ord(char) >= 6 and ord(char) <= 70)])
