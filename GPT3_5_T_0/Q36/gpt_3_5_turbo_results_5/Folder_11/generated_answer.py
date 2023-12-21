
def filter_chars(string):
    return string[:86] + string[93:].replace('E', '').replace('~', '')
