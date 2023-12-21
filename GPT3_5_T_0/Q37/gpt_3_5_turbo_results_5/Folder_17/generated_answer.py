
def filter_chars(string):
    return string[:27] + string[27:30].replace(';', '').replace('b', '') + string[30:]
