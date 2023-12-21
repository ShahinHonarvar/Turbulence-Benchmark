
def filter_chars(string):
    for i in range(43, 69):
        if string[i].isalpha() and 'B' < string[i] < 'r':
            string = string.replace(string[i], '')
    return string
