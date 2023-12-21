
def filter_chars(string):
    result = ''
    for i, c in enumerate(string):
        if (i >= 7 and i <= 8) and 'B' <= c <= 'H':
            continue
        result += c
    return result
