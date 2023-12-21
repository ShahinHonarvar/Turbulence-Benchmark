
def filter_chars(string):
    return string[:34] + ''.join(c for c in string[34:68] if not 'W' <= c <= 'x') + string[68:]
