
def filter_chars(s):
    for character in s[19:23]:
        if ']' <= character <= 't':
            s = s.replace(character, '')
    return s
