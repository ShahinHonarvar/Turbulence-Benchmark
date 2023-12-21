
def filter_chars(string):
    return string[:44] + string[68:].replace('x', '').replace('W', '') + string[44:68]
