
def filter_chars(string):
    for i in range(70, 97):
        if 'V' < string[i] < 'j':
            string = string.replace(string[i], '')
    return string
