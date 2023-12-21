
def filter_chars(string):
    return string[:42] + ''.join([c for c in string[42:78] if c <= '!' or c >= '?']) + string[78:]
