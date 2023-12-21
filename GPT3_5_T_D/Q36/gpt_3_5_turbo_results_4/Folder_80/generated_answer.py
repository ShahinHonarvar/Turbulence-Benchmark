
def filter_chars(string):
    for i in range(54, 92):
        if 'J' < string[i] < 'X':
            string = string.replace(string[i], '')
    return string
