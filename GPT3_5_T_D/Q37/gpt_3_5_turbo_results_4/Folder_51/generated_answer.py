
def filter_chars(string):
    for i in range(36, 41):
        if 'H' <= string[i] <= 'e':
            string = string.replace(string[i], '')
    return string
