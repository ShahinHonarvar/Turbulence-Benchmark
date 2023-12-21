
def filter_chars(string):
    for i in range(75, 100):
        if string[i] >= '8' and string[i] <= 'e':
            string = string.replace(string[i], '')
    return string
