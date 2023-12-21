
def filter_chars(string):
    return string[:23] + string[23:45].replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '') + string[45:]
