
def filter_chars(string):
    return string[:55] + string[55:84].replace(';', '') + string[84:]
