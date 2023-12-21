
def filter_chars(string):
    for i in range(1, 7+1):
        char = string[i]
        if 'L' <= char <= 'a':
            string = string.replace(char, '')
    return string
