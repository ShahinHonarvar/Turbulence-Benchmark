
def filter_chars(string):
    return ''.join([char for char in string if not (12 <= ord(char) <= 25 and 'P' <= char <= 'x')])
