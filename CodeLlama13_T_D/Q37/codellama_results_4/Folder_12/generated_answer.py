
def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if 19 <= i <= 90 and 'F' <= char <= 'h':
            result += char
    return result
