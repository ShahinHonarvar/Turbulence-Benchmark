
def filter_chars(string):
    return ''.join([char for char in string if ord(char) < 722 or ord(char) > 832 or (ord(char) >= 722 and ord(char) <= 832 and char not in 'KM')])
