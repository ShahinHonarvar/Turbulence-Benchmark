
def filter_chars(string):
    return string[:81] + string[81:86].replace('!', '').replace('s', '') + string[86:]
