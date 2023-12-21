
def filter_chars(string):
    for i in range(19, 23):
        char = string[i]
        if ']' <= char <= 't':
            string = string.replace(char, '')
    return string
