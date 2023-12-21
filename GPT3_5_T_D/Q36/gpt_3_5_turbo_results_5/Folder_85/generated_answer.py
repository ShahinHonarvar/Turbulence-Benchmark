
def filter_chars(string):
    return string[:55] + string[55:80].replace('S', '').replace('s', '') + string[80:]
