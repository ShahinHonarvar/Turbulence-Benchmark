
def filter_chars(string):
    return ''.join([char for char in string if not (26 <= ord(char) <= 64 and 'V' <= char <= 'o')])
