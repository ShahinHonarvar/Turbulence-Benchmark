
def filter_chars(string):
    return string[:35] + ''.join([char for char in string[35:41] if ')' <= char <= 'l']) + string[41:]
