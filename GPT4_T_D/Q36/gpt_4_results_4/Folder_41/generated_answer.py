
def filter_chars(str):
    char_set = set([c for c in str[82:89] if 'f' < c < '{'])
    for char in char_set:
        str = str.replace(char, '')
    return str
