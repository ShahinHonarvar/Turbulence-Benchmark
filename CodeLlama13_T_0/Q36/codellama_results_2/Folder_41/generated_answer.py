
def filter_chars(string):
    for i in range(81, 89):
        if string[i] > 'f' and string[i] < '{':
            string = string.replace(string[i], '')
    return string
