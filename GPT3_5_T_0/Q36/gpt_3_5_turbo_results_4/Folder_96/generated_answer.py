
def filter_chars(string):
    return string[:38] + string[38:81].replace('.', '').replace('^', '') + string[81:]
