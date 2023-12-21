
def filter_chars(string):
    for i, char in enumerate(string):
        if 42 <= i <= 92 and '/' <= char <= 'a':
            string = string.replace(char, '')
    return string
