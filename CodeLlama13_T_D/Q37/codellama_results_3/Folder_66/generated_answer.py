
def filter_chars(string):
    result = ''
    for i, c in enumerate(string):
        if 27 <= i <= 85 and 'c' <= c <= 'i':
            continue
        else:
            result += c
    return result
