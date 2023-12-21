
def filter_chars(string):
    return string[:73] + string[74:].replace('U', '').replace('V', '').replace('W', '').replace('X', '').replace('Y', '').replace('Z', '').replace('[', '').replace('\\', '').replace(']', '').replace('^', '').replace('_', '').replace('`', '').replace('a', '').replace('b', '').replace('c', '').replace('d', '').replace('e', '').replace('f', '').replace('g', '').replace('h', '').replace('i', '').replace('j', '').replace('k', '').replace('l', '')
