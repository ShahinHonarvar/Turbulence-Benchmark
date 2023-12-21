
def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if 63 <= ord(c) <= 84 and 'E' <= c <= '~':
            continue
        result += c
    return result
