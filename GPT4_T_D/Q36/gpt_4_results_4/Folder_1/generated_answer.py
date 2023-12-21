
def filter_chars(s):
    for character in s[70:87]:
        if '#' < character < 'L':
            s = s.replace(character, '')
    return s
