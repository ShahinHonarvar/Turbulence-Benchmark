
def filter_chars(string):
    return string[:78] + string[81:].replace('T', '').replace('U', '').replace('V', '') + string[81:]
