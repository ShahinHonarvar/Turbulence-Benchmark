
def filter_chars(string):
    filtered = ''
    for i in range(15, 56):
        char = string[i]
        if 'W' <= char <= '{':
            filtered += char
    return filtered
