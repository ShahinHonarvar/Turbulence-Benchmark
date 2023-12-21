
def filter_chars(string):
    result = ''
    for index, char in enumerate(string):
        if 1 <= index <= 7 and 'L' <= char <= 'a':
            string = string.replace(char, '')
        else:
            result += char
    return result
