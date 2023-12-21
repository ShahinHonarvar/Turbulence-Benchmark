
def filter_chars(s):
    chars_to_remove = set([char for char in s[722:833] if 'K' <= char <= 'm'])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
