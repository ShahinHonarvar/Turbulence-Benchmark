
def filter_chars(string):
    return "".join([char for char in string if (ord(char) < ord('H') and ord(char) >= ord('B'))])
