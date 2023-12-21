
def filter_chars(string):
    return string[:8] + string[10:].replace(string[8:10], "")
