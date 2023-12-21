
def filter_chars(string):
    return string[:72] + string[93:].replace('<', '').replace('J', '')
