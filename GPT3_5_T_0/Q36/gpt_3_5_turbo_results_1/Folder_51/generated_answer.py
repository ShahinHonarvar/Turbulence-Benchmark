
def filter_chars(string):
    return string[:58] + string[81:].replace('6', '').replace('7', '').replace('8', '').replace('9', '') + string[81:]
