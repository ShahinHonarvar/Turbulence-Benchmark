
def filter_chars(string):
    return string[:170] + string[170:195].replace('!', '').replace('}', '') + string[195:]
