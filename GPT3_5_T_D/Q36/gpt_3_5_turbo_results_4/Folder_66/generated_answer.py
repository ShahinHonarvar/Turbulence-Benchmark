
def filter_chars(string):
    return string[:39] + string[39:87].replace('!', '').replace('}', '') + string[87:]
