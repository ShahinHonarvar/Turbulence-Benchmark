
def filter_chars(string):
    return string[:77] + string[77:87].replace(';', '').replace('r', '') + string[87:]
