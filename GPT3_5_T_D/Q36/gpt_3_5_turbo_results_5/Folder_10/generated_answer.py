
def filter_chars(string):
    return string[:35] + string[35:60].replace('!', '').replace('"', '').replace('#', '').replace('$', '').replace('%', '') + string[60:]
