
def filter_chars(string):
    return string[:29] + ''.join(c for c in string[29:80] if not ('K' <= c <= 'z')) + string[80:]
