
def filter_chars(string):
    return string[:770] + string[771:971].replace('-', '') + string[971:]
