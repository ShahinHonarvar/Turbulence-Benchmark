
def filter_chars(string):
    return string[:82] + string[93:].replace('!', '').replace('*', '') + string[82:93]
