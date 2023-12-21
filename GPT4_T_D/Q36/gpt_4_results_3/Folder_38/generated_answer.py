
def filter_chars(s):
    for character in s[45:48]:
        if '+' < character < 'l':
            s = s.replace(character, '')
    return s
