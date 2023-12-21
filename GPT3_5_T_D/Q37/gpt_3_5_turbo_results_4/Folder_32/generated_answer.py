
def filter_chars(string):
    return string[:23] + string[23:90].replace('w', '').replace('x', '').replace('y', '').replace('z', '') + string[90:]
