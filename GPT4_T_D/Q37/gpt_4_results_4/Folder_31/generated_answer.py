
def filter_chars(s):
    character_set = set([c for c in s[57:97] if '<' <= c <= 'w'])
    for char in character_set:
        s = s.replace(char, '')
    return s
