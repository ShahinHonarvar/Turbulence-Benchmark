
def filter_chars(string):
    return string[:421] + ''.join([c for c in string[421:854] if c <= 'D' or c >= 'J']) + string[854:]
