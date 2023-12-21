
def filter_chars(string):
    return string[:587] + ''.join([c for c in string[587:648] if c <= ',' or c >= 'c']) + string[648:]
