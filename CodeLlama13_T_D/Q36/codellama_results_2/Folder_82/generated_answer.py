
def filter_chars(string):
    for i in range(69, 97):
        if string[i] > 'V' and string[i] < 'j':
            string = string.replace(string[i], '')
    return string
