
def filter_chars(string):
    return string[:42] + string[42:67].replace('7', '').replace('8', '').replace('9', '') + string[67:]
