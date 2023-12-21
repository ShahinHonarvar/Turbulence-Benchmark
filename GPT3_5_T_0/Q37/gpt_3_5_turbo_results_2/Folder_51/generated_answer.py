
def filter_chars(string):
    return string[:36] + string[36:41].replace('H', '').replace('I', '').replace('J', '').replace('K', '').replace('L', '').replace('M', '').replace('N', '').replace('O', '').replace('P', '').replace('Q', '').replace('R', '').replace('S', '').replace('T', '').replace('U', '').replace('V', '').replace('W', '').replace('X', '').replace('Y', '').replace('Z', '').replace('[', '').replace('\\', '').replace(']', '').replace('^', '').replace('_', '').replace('`', '').replace('a', '').replace('b', '').replace('c', '').replace('d', '').replace('e', '') + string[41:]
