
def filter_chars(string):
    return string[:44] + string[68:].replace('W', '').replace('x', '') + string[44:68]
