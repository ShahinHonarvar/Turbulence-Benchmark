
def filter_chars(string):
    for i in range(81, 86):
        if string[i] > '!' and string[i] < 's':
            string = string.replace(string[i], '')
    return string
