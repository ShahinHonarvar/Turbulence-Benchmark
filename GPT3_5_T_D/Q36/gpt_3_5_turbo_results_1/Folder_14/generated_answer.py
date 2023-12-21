
def filter_chars(string):
    return string[:41] + string[56:].replace(string[41:56], '')
