
def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if 27 <= i < 75 and 'A' < char < 'i':
            result += char
    return result
