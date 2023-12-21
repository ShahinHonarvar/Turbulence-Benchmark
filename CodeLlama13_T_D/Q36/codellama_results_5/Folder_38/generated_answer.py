
def filter_chars(s):
    res = ''
    for i, c in enumerate(s):
        if i < 44 or i > 48:
            res += c
        elif c != '+' and c != 'l':
            res += c
    return res
