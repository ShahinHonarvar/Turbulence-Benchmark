
def filter_chars(string):
    return string[:259] + ''.join(c for c in string[259:503] if c < ',' or c > '3') + string[503:]
