
def filter_chars(string):
    for i in range(63, 85):
        char = chr(i)
        if char >= 'E' and char <= '~':
            string = string.replace(char, '')
    return string
