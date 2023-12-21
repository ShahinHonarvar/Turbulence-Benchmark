
def filter_chars(string):
    result = ''
    for i, c in enumerate(string):
        if 38 <= i <= 54 and ':' <= c <= 'r':
            continue
        else:
            result += c
    return result
