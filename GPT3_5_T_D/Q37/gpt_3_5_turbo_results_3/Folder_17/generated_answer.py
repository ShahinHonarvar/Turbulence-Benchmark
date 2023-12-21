
def filter_chars(string):
    return string[:27] + string[30:].replace(';', '').replace('b', '') + string[27:30].replace(string[27:30], '')
