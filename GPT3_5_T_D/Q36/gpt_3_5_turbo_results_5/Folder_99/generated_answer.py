
def filter_chars(string):
    return string[:476] + string[476:948].replace('c', '') + string[948:]
