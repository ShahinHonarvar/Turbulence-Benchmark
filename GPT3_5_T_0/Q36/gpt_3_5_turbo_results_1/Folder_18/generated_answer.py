
def filter_chars(string):
    return string[:587] + ''.join([char for char in string[587:648] if char <= ',' or char >= 'c']) + string[648:]
