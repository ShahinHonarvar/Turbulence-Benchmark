
def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if not (71 <= i <= 96 and '_' <= char <= 'o'):
            result += char
    return result
