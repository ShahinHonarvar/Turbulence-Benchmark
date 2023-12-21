
def filter_chars(string):
    if len(string) < 100:
        return string
    else:
        return string[:83] + string[83:100].replace('*', '') + string[100:]
