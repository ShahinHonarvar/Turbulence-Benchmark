
def filter_chars(string):
    return string[:81] + ''.join(c for c in string[81:89] if not ('f' < c < '{')) + string[89:]
