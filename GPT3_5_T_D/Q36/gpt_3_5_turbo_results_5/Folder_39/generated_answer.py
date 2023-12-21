
def filter_chars(string):
    return string[:43] + string[43:59].replace('6', '').replace('7', '').replace('8', '').replace('9', '') + string[59:]
