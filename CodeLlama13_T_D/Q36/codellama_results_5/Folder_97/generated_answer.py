
def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if i < 309 or i > 591:
            result += char
        elif char <= 'S' or char >= 'm':
            result += char
        else:
            result += char
    return result
