
def filter_chars(string):
    for index in range(19, min(93, len(string))):
        char = string[index]
        if '8' <= char <= 'm':
            string = string.replace(char, '')
    return string
