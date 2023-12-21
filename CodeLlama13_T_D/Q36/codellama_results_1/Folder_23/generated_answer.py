
def filter_chars(string):
    for i in range(21, 26):
        if string[i] > '5' and string[i] < '}':
            string = string.replace(string[i], '')
    return string
