
def filter_chars(string):
    return string[:20] + ''.join(char for char in string[20:63] if not ('i' <= char <= 'k')) + string[63:]
