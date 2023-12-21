
def filter_chars(string):
    return string[:41] + string[86+1:] + ''.join(c for c in string[41:86+1] if c < 'S' or c > 's')
