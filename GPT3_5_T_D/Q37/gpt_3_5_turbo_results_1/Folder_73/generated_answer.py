
def filter_chars(string):
    for char in string[22:86]:
        if '7' <= char <= 'e':
            string = string.replace(char, '')
    return string
