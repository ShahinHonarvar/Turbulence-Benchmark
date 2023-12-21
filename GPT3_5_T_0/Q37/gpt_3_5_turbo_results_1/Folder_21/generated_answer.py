
def filter_chars(string):
    return string[:603] + ''.join([c for c in string[603:760] if not ('Q' <= c <= 'h')]) + string[760:]
