
def filter_chars(string):
    for i in range(24, 79+1):
        if string[i].isalpha() and 'a' <= string[i] <= 'f':
            string = string.replace(string[i], '')
    return string
