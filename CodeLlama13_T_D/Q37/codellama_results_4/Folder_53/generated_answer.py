
def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if (83 <= ord(char) <= 99) and ('*' <= char <= 'j'):
            continue
        result += char
    return result
