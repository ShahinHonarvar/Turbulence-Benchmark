
def filter_chars(string):
    for i in range(4, 5):
        if string[i] >= '7' and string[i] <= 'o':
            string = string.replace(string[i], '')
    return string
