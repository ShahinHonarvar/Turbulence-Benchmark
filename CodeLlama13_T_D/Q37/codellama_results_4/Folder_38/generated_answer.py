
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 24 or i > 79 or char < 'a' or char > 'f':
            result += char
    return result
