
def filter_chars(s):
    for character in s[259:503]:
        if ',' <= character <= '3':
            s = s.replace(character, '')
    return s
