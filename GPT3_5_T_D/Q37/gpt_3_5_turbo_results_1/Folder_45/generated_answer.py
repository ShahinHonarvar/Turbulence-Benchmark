
def filter_chars(string):
    return string[:72] + string[95:].replace('.', '').replace('a', '').replace('b', '')
