
def filter_chars(string):
    for i in range(502, 946):
        char = string[i]
        if char > 'W' and char < 'y':
            string = string.replace(char, '')
    return string
