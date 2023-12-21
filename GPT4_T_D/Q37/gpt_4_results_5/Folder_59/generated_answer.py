
def filter_chars(string):
    char_set = {c for c in string[2:4] if '5' <= c <= '_'}
    return ''.join(c for c in string if c not in char_set)
