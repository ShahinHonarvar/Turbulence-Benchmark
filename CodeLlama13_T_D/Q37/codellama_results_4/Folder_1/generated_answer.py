
def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if 41 <= i <= 79 and 'f' <= c <= '|':
            continue
        result += c
    return result
