
def filter_chars(string):
    return string[:603] + string[603:760].replace('Q', '').replace('R', '').replace('S', '').replace('T', '').replace('U', '').replace('V', '').replace('W', '').replace('X', '').replace('Y', '').replace('Z', '').replace('[', '').replace('\\', '').replace(']', '').replace('^', '').replace('_', '').replace('`', '').replace('a', '').replace('b', '').replace('c', '').replace('d', '').replace('e', '').replace('f', '').replace('g', '').replace('h', '') + string[760:]
