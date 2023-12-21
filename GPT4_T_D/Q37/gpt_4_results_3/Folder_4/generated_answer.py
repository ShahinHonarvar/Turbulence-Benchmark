
def filter_chars(string):
    for char in string[19:34]:
        if 'S' <= char <= '{':
            string = string.replace(char, '')
    return string
