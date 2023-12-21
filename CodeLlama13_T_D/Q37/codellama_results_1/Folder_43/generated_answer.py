
def filter_chars(string):
    result = ''
    for i, c in enumerate(string):
        if 15 <= i <= 55 and 'W' <= c <= '{':
            result += c
    return result
