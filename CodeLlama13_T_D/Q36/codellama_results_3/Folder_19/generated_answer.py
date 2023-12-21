
def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if (i < 77 or i > 87) and char not in ';r':
            result += char
    return result
