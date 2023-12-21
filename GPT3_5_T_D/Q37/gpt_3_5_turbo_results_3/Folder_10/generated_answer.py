
def filter_chars(string):
    for i in range(63, 85):
        char = chr(i)
        if 'E' <= char <= '~':
            string = string.replace(char, '')
    return string
