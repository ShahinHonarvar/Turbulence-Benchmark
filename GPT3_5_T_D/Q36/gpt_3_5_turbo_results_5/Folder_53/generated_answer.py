
def filter_chars(string):
    return string.replace('k', '').replace('l', '').replace('m', '').replace('n', '').replace('o', '').replace('p', '').replace('q', '').replace('r', '').replace('s', '').replace('t', '')[0:90] + string[90:97] + string[97:]
