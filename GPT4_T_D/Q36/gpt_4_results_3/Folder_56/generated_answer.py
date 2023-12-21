
def filter_chars(s):
    for character in s[32:50]:
        if '/' < character < 'J':
            s = s.replace(character, "")
    return s
