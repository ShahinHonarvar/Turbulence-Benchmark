
def filter_chars(string):
    char_set = set(string[15:75])
    for ch in char_set:
        if '9' < ch < 'K':
            string = string.replace(ch, '')     
    return string
