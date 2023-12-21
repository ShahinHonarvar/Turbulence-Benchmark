
def filter_chars(string):
    return string[:10] + ''.join([c for c in string[10:15] if c <= 't' or c >= 'v']) + string[15:]
