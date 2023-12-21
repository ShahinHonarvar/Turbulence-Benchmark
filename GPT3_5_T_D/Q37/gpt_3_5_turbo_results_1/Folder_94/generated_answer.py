
def filter_chars(string):
    return ''.join([char for char in string if not (51 <= ord(char) <= 96 and 'X' <= char <= 'p')])
