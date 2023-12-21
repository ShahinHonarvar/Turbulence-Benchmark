
def filter_chars(string):
    return string[:14] + string[14:75].replace('9', '').replace(':', '').replace(';', '').replace('<', '').replace('=', '').replace('>', '') + string[75:]
