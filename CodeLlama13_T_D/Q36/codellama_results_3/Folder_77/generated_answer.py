
def filter_chars(string):
    for i in range(221, 419):
        char = string[i]
        if char > '-' and char < 'v':
            string = string.replace(char, '')
    return string
