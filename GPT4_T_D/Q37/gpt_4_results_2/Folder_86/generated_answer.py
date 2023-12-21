
def filter_chars(s):
    char_set = set(s[164:707])
    char_set = {c for c in char_set if 'O' <= c <= '}'}
    for c in char_set:
        s = s.replace(c, '')
    return s
