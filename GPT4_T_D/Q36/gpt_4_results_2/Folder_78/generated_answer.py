
def filter_chars(s):
    for character in s[30:33]:
        if '%' < character < 'a':
            s = s.replace(character, '')
    return s
