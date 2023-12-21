
def filter_chars(string):
    result = ''
    for i, c in enumerate(string):
        if (36 <= i < 79) and ('a' <= c <= 'i'):
            result += c
    return result
