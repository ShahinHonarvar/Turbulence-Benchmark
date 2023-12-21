
def filter_chars(string):
    for i in range(70, 75):
        if string[i].isalpha() and 'A' < string[i] < 'U':
            string = string.replace(string[i], '')
    return string
