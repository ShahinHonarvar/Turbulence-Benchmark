
def filter_chars(string):
    for i in range(373, 901):
        char = string[i]
        if 'T' <= char <= 'h':
            string = string.replace(char, '')
    return string
