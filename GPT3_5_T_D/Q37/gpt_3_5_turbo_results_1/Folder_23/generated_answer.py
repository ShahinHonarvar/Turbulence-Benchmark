
def filter_chars(string):
    return ''.join([char for char in string if not (51 <= string.index(char) <= 77 and 'V' <= char <= 'Y')])
