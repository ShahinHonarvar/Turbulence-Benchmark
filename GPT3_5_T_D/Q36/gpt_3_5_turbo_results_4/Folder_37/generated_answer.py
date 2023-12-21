
def filter_chars(string):
    return string[:44] + string[59:].replace('/', '').replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '') + string[59:]
