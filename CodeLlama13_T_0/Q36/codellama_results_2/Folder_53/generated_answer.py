
def filter_chars(string):
    for i in range(90, 97):
        if string[i] > 'j' and string[i] < 'w':
            string = string.replace(string[i], '')
    return string
