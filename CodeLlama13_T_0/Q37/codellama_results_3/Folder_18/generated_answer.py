
def filter_chars(string):
    return ''.join([char for char in string if ord(char) < 770 or ord(char) > 970 or (ord(char) >= ord('-') and ord(char) <= ord('D'))])
