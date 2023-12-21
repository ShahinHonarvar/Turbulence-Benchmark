
def filter_chars(string):
    return string[:171] + ''.join([c for c in string[171:636] if c <= 'c' or c >= 's']) + string[636:]
