
def filter_chars(string):
    return string[:29] + string[33:].replace('%', '').replace('`', '')
