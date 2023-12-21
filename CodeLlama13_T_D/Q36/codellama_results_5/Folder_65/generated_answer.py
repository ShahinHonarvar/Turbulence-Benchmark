
def filter_chars(string):
    for i in range(58, 82):
        if string[i].isalpha() and 'F' < string[i] < 'O':
            string = string.replace(string[i], '')
    return string
