
def filter_chars(string):
    return string[:31] + string[50:].replace('', '').replace('/', '').replace('J', '') + string[31:50]
