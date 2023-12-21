
def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if 86 <= ord(char) <= 92 and char >= '!' and char <= 's':
            result += char
        else:
            result += char
    return result
