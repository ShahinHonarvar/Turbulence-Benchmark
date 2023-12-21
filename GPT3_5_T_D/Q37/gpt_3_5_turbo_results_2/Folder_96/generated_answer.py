
def filter_chars(string):
    return string[:86] + string[86:93].replace('!', '') + string[93:]
