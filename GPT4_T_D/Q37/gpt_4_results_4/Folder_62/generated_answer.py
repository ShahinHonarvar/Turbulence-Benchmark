
def filter_chars(s):
    for char in set(s[10:70]):
        if char >= 'I' and char <= 'K':
            s = s.replace(char, '')
    return s
