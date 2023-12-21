
def filter_chars(string):
    return ''.join([char for char in string if not (7 <= ord(char) - 65 < 8 and 'B' <= char <= 'H')])
