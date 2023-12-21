
def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if i < 43 or i > 69:
            result += char
    return result
