
def filter_chars(string):
    return string[:51] + ''.join([c for c in string[51:78] if c < 'V' or c > 'Y']) + string[78:]
