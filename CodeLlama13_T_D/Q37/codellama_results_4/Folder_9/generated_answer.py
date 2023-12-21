
def filter_chars(string):
    result = ''
    for i, c in enumerate(string):
        if 38 <= i <= 99 and 'A' <= c <= 'Q':
            result += c
    return result
