
def filter_chars(string):
    for i in range(12, 78):
        char = string[i]
        if ':' <= char <= 'L':
            string = string.replace(char, '')
    return string
