
def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if i < 55 or i > 66:
            result += c
        elif c > 'f' and c < '|':
            result += c
    return result
