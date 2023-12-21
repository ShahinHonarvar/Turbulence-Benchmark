
def filter_chars(string):
    for i in range(219, 403):
        if '*' < string[i] < '7':
            string = string.replace(string[i], '')
    return string
