
def filter_chars(string):
    return string[:225] + ''.join([c for c in string[225:382] if c < 'D' or c > 'Y']) + string[382:]
