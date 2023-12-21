
def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if 12 <= i <= 25 and 'P' <= c <= 'x':
            continue
        result += c
    return result
