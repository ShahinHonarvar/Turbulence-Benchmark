
def filter_chars(string):
    result = ''
    for i, c in enumerate(string):
        if i < 384 or i > 411:
            result += c
    return result
