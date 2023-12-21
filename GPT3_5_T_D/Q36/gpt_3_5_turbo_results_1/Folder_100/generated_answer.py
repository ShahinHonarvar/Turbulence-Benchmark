
def filter_chars(string):
    return string[:43] + ''.join([c for c in string[43:69] if not 'B' < c < 'r']) + string[69:]
