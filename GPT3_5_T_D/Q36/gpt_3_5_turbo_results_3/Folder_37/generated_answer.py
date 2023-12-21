
def filter_chars(string):
    return string[:44] + string[59:].replace(string[44:59], "")
