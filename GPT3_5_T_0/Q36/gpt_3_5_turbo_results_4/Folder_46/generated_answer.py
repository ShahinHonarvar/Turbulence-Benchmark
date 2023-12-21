
def filter_chars(string):
    return string[:19] + string[69:] + ''.join(c for c in string[19:69] if not ('<' < c < 'C'))
