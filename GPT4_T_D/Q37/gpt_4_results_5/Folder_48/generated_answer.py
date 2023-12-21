
def filter_chars(string):
    for char in string[513:878]:
        if '?' <= char <= 'n':
            string = string.replace(char, '')
    return string
